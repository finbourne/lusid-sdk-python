# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.5001
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


class BatchAdjustHoldingsResponse(object):
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
        'values': 'dict(str, HoldingAdjustmentWithDate)',
        'failed': 'dict(str, ErrorDetail)',
        'metadata': 'dict(str, list[ResponseMetaData])',
        'links': 'list[Link]'
    }

    attribute_map = {
        'values': 'values',
        'failed': 'failed',
        'metadata': 'metadata',
        'links': 'links'
    }

    required_map = {
        'values': 'optional',
        'failed': 'optional',
        'metadata': 'optional',
        'links': 'optional'
    }

    def __init__(self, values=None, failed=None, metadata=None, links=None, local_vars_configuration=None):  # noqa: E501
        """BatchAdjustHoldingsResponse - a model defined in OpenAPI"
        
        :param values:  The holdings which have been successfully adjusted.
        :type values: dict[str, lusid.HoldingAdjustmentWithDate]
        :param failed:  The holdings that could not be adjusted along with a reason for their failure.
        :type failed: dict[str, lusid.ErrorDetail]
        :param metadata:  Contains warnings related to adjusted holdings
        :type metadata: dict(str, list[ResponseMetaData])
        :param links:  Collection of links.
        :type links: list[lusid.Link]

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._values = None
        self._failed = None
        self._metadata = None
        self._links = None
        self.discriminator = None

        self.values = values
        self.failed = failed
        self.metadata = metadata
        self.links = links

    @property
    def values(self):
        """Gets the values of this BatchAdjustHoldingsResponse.  # noqa: E501

        The holdings which have been successfully adjusted.  # noqa: E501

        :return: The values of this BatchAdjustHoldingsResponse.  # noqa: E501
        :rtype: dict[str, lusid.HoldingAdjustmentWithDate]
        """
        return self._values

    @values.setter
    def values(self, values):
        """Sets the values of this BatchAdjustHoldingsResponse.

        The holdings which have been successfully adjusted.  # noqa: E501

        :param values: The values of this BatchAdjustHoldingsResponse.  # noqa: E501
        :type values: dict[str, lusid.HoldingAdjustmentWithDate]
        """

        self._values = values

    @property
    def failed(self):
        """Gets the failed of this BatchAdjustHoldingsResponse.  # noqa: E501

        The holdings that could not be adjusted along with a reason for their failure.  # noqa: E501

        :return: The failed of this BatchAdjustHoldingsResponse.  # noqa: E501
        :rtype: dict[str, lusid.ErrorDetail]
        """
        return self._failed

    @failed.setter
    def failed(self, failed):
        """Sets the failed of this BatchAdjustHoldingsResponse.

        The holdings that could not be adjusted along with a reason for their failure.  # noqa: E501

        :param failed: The failed of this BatchAdjustHoldingsResponse.  # noqa: E501
        :type failed: dict[str, lusid.ErrorDetail]
        """

        self._failed = failed

    @property
    def metadata(self):
        """Gets the metadata of this BatchAdjustHoldingsResponse.  # noqa: E501

        Contains warnings related to adjusted holdings  # noqa: E501

        :return: The metadata of this BatchAdjustHoldingsResponse.  # noqa: E501
        :rtype: dict(str, list[ResponseMetaData])
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this BatchAdjustHoldingsResponse.

        Contains warnings related to adjusted holdings  # noqa: E501

        :param metadata: The metadata of this BatchAdjustHoldingsResponse.  # noqa: E501
        :type metadata: dict(str, list[ResponseMetaData])
        """

        self._metadata = metadata

    @property
    def links(self):
        """Gets the links of this BatchAdjustHoldingsResponse.  # noqa: E501

        Collection of links.  # noqa: E501

        :return: The links of this BatchAdjustHoldingsResponse.  # noqa: E501
        :rtype: list[lusid.Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this BatchAdjustHoldingsResponse.

        Collection of links.  # noqa: E501

        :param links: The links of this BatchAdjustHoldingsResponse.  # noqa: E501
        :type links: list[lusid.Link]
        """

        self._links = links

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
        if not isinstance(other, BatchAdjustHoldingsResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BatchAdjustHoldingsResponse):
            return True

        return self.to_dict() != other.to_dict()