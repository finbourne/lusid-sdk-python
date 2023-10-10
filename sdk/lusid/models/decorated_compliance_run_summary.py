# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 1.0.595
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


class DecoratedComplianceRunSummary(object):
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
        'run_id': 'ResourceId',
        'details': 'list[ComplianceRuleResultDetail]'
    }

    attribute_map = {
        'run_id': 'runId',
        'details': 'details'
    }

    required_map = {
        'run_id': 'required',
        'details': 'required'
    }

    def __init__(self, run_id=None, details=None, local_vars_configuration=None):  # noqa: E501
        """DecoratedComplianceRunSummary - a model defined in OpenAPI"
        
        :param run_id:  (required)
        :type run_id: lusid.ResourceId
        :param details:  (required)
        :type details: list[lusid.ComplianceRuleResultDetail]

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._run_id = None
        self._details = None
        self.discriminator = None

        self.run_id = run_id
        self.details = details

    @property
    def run_id(self):
        """Gets the run_id of this DecoratedComplianceRunSummary.  # noqa: E501


        :return: The run_id of this DecoratedComplianceRunSummary.  # noqa: E501
        :rtype: lusid.ResourceId
        """
        return self._run_id

    @run_id.setter
    def run_id(self, run_id):
        """Sets the run_id of this DecoratedComplianceRunSummary.


        :param run_id: The run_id of this DecoratedComplianceRunSummary.  # noqa: E501
        :type run_id: lusid.ResourceId
        """
        if self.local_vars_configuration.client_side_validation and run_id is None:  # noqa: E501
            raise ValueError("Invalid value for `run_id`, must not be `None`")  # noqa: E501

        self._run_id = run_id

    @property
    def details(self):
        """Gets the details of this DecoratedComplianceRunSummary.  # noqa: E501


        :return: The details of this DecoratedComplianceRunSummary.  # noqa: E501
        :rtype: list[lusid.ComplianceRuleResultDetail]
        """
        return self._details

    @details.setter
    def details(self, details):
        """Sets the details of this DecoratedComplianceRunSummary.


        :param details: The details of this DecoratedComplianceRunSummary.  # noqa: E501
        :type details: list[lusid.ComplianceRuleResultDetail]
        """
        if self.local_vars_configuration.client_side_validation and details is None:  # noqa: E501
            raise ValueError("Invalid value for `details`, must not be `None`")  # noqa: E501

        self._details = details

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
        if not isinstance(other, DecoratedComplianceRunSummary):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DecoratedComplianceRunSummary):
            return True

        return self.to_dict() != other.to_dict()