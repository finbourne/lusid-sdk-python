# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 1.0.540
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from lusid.configuration import Configuration


class OrderFlowConfiguration(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
      required_map (dict): The key is attribute name
                           and the value is whether it is 'required' or 'optional'.
    """
    openapi_types = {
        'include_entity_types': 'str'
    }

    attribute_map = {
        'include_entity_types': 'includeEntityTypes'
    }

    required_map = {
        'include_entity_types': 'required'
    }

    def __init__(self, include_entity_types=None, local_vars_configuration=None):  # noqa: E501
        """OrderFlowConfiguration - a model defined in OpenAPI"
        
        :param include_entity_types:  (required)
        :type include_entity_types: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._include_entity_types = None
        self.discriminator = None

        self.include_entity_types = include_entity_types

    @property
    def include_entity_types(self):
        """Gets the include_entity_types of this OrderFlowConfiguration.  # noqa: E501


        :return: The include_entity_types of this OrderFlowConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._include_entity_types

    @include_entity_types.setter
    def include_entity_types(self, include_entity_types):
        """Sets the include_entity_types of this OrderFlowConfiguration.


        :param include_entity_types: The include_entity_types of this OrderFlowConfiguration.  # noqa: E501
        :type include_entity_types: str
        """
        if self.local_vars_configuration.client_side_validation and include_entity_types is None:  # noqa: E501
            raise ValueError("Invalid value for `include_entity_types`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                include_entity_types is not None and len(include_entity_types) < 1):
            raise ValueError("Invalid value for `include_entity_types`, length must be greater than or equal to `1`")  # noqa: E501

        self._include_entity_types = include_entity_types

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = getfullargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, OrderFlowConfiguration):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OrderFlowConfiguration):
            return True

        return self.to_dict() != other.to_dict()