# lusid.LoginApi

All URIs are relative to *http://local-unit-test-server.lusid.com:44717*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_saml_identity_provider_id**](LoginApi.md#get_saml_identity_provider_id) | **GET** /api/login/saml/{domain} | GetSamlIdentityProviderId: Get SAML Identity Provider


# **get_saml_identity_provider_id**
> str get_saml_identity_provider_id(domain)

GetSamlIdentityProviderId: Get SAML Identity Provider

Get the unique identifier for the SAML 2.0 Identity Provider to be used for domain.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://local-unit-test-server.lusid.com:44717
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid.Configuration(
    host = "http://local-unit-test-server.lusid.com:44717"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid.Configuration(
    host = "http://local-unit-test-server.lusid.com:44717"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.LoginApi(api_client)
    domain = 'domain_example' # str | The domain that the user will be logging in to

    try:
        # GetSamlIdentityProviderId: Get SAML Identity Provider
        api_response = api_instance.get_saml_identity_provider_id(domain)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LoginApi->get_saml_identity_provider_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| The domain that the user will be logging in to | 

### Return type

**str**

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The ID of the SAML Identity Provider to be used (may be null) |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

