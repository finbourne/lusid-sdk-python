import functools
import importlib
import inspect

from lusid import ApiClient
from lusid.utilities.api_client_builder import ApiClientBuilder
from lusid.utilities.proxy_config import ProxyConfig
from lusid.utilities.api_configuration import ApiConfiguration
from lusid.utilities.lusid_retry import lusidretry


class ApiClientFactory:
    """
    The ApiClientFactory is responsible for providing the ability to create any of the LUSID APIs using the provided
    credentials. It will use the same ApiClient across all of the APIs.

    """
    def __init__(self, **kwargs):
        """
        Iniitalise an ApiClientFactory by passing the token, api_url and app_name, or by
        passing in the api_secrets_filename

        :param str token: Bearer token used to initialise the API
        :param str api_secrets_filename: Name of secrets file (including full path)
        :param str api_url: LUSID API url
        :param str app_name: Application name (optional)
        :param str certificate_filename: Name of the certificate file (.pem, .cer or .crt)
        :param str proxy_url: The url of the proxy to use including the port e.g. http://myproxy.com:8888
        :param str proxy_username: The username for the proxy to use
        :param str proxy_password: The password for the proxy to use
        """

        builder_kwargs = {}

        if "token" in kwargs and str(kwargs["token"]) != "None":
            # If there is a token use it along with the specified proxy details if specified
            config = ApiConfiguration(
                api_url=kwargs.get("api_url", None),
                certificate_filename=kwargs.get("certificate_filename", None),
                proxy_config=ProxyConfig(
                    address=kwargs.get("proxy_url", None),
                    username=kwargs.get("proxy_username", None),
                    password=kwargs.get("proxy_password", None),
                ) if kwargs.get("proxy_url", None) is not None else None,
                app_name=kwargs.get("app_name", None)
            )

            builder_kwargs["api_configuration"] = config
            builder_kwargs["token"] = kwargs["token"]

        # Otherwise use a secrets file if it exists
        builder_kwargs["api_secrets_filename"] = kwargs.get("api_secrets_filename", None)

        # Call the client builder, this will result in using either a token, secrets file or environment variables
        self.api_client = ApiClientBuilder.build(**builder_kwargs)

    def build(self, metaclass):
        """
        :param type metaclass:  type of the LUSID API to create
        :return: Initalised LUSID API for the type passed in
        """

        def get_attribute_impl(source_obj, name):
            """
            Implementation of __getattribute__ that adds a decorator that adds a call_info
            argument to return additional call stats
            """

            attr = super(metaclass, source_obj).__getattribute__(name)

            @functools.wraps(attr)
            @lusidretry
            def wrapper(*args, **kwargs):
                def is_http_info_method(m):
                    return inspect.ismethod(m) and m.__name__.endswith(
                        "_with_http_info"
                    )

                if kwargs.get("call_info") is not None:
                    callback = kwargs.pop("call_info")

                    if not inspect.isfunction(callback):
                        raise ValueError("call_info value must be a lambda")

                    if is_http_info_method(attr):
                        result = attr(*args, **kwargs)
                    else:
                        #   switch to the '_with_http_info' implementation
                        func = getattr(source_obj, f"{name}_with_http_info")
                        result = func(*args, **kwargs)

                    # pass the http info to caller
                    callback(result[2])

                    # return the dto
                    return result[0]

                else:
                    return attr(*args, **kwargs)

            return wrapper if inspect.ismethod(attr) else attr

        def init_impl(dest, src=None):
            if type(dest) == type(src):
                dest.__dict__ = src.__dict__
            elif type(src) == ApiClient:
                dest.api_client = src

        module = importlib.import_module("lusid.api")
        api_name = metaclass.__name__

        if not api_name.endswith("Api") or not hasattr(module, api_name):
            raise TypeError(f"unknown api: {api_name}")

        # create an instance of the api
        api_impl = getattr(module, api_name)(self.api_client)

        setattr(metaclass, "__getattribute__", get_attribute_impl)
        setattr(metaclass, "__init__", init_impl)

        return api_impl
