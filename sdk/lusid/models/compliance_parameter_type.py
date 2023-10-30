# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    Contact: info@finbourne.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import json
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class ComplianceParameterType(str, Enum):
    """
    ComplianceParameterType
    """

    """
    allowed enum values
    """
    BOOLCOMPLIANCEPARAMETER = 'BoolComplianceParameter'
    STRINGCOMPLIANCEPARAMETER = 'StringComplianceParameter'
    DECIMALCOMPLIANCEPARAMETER = 'DecimalComplianceParameter'
    DATETIMECOMPLIANCEPARAMETER = 'DateTimeComplianceParameter'
    PROPERTYKEYCOMPLIANCEPARAMETER = 'PropertyKeyComplianceParameter'
    ADDRESSKEYCOMPLIANCEPARAMETER = 'AddressKeyComplianceParameter'
    PORTFOLIOIDCOMPLIANCEPARAMETER = 'PortfolioIdComplianceParameter'
    PORTFOLIOGROUPIDCOMPLIANCEPARAMETER = 'PortfolioGroupIdComplianceParameter'
    STRINGLISTCOMPLIANCEPARAMETER = 'StringListComplianceParameter'
    BOOLLISTCOMPLIANCEPARAMETER = 'BoolListComplianceParameter'
    DATETIMELISTCOMPLIANCEPARAMETER = 'DateTimeListComplianceParameter'
    DECIMALLISTCOMPLIANCEPARAMETER = 'DecimalListComplianceParameter'
    PROPERTYKEYLISTCOMPLIANCEPARAMETER = 'PropertyKeyListComplianceParameter'
    ADDRESSKEYLISTCOMPLIANCEPARAMETER = 'AddressKeyListComplianceParameter'
    PORTFOLIOIDLISTCOMPLIANCEPARAMETER = 'PortfolioIdListComplianceParameter'
    PORTFOLIOGROUPIDLISTCOMPLIANCEPARAMETER = 'PortfolioGroupIdListComplianceParameter'
    INSTRUMENTLISTCOMPLIANCEPARAMETER = 'InstrumentListComplianceParameter'

    @classmethod
    def from_json(cls, json_str: str) -> ComplianceParameterType:
        """Create an instance of ComplianceParameterType from a JSON string"""
        return ComplianceParameterType(json.loads(json_str))