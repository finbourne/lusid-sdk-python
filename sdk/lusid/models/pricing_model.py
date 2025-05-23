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





class PricingModel(str, Enum):
    """
    PricingModel
    """

    """
    allowed enum values
    """
    SIMPLESTATIC = 'SimpleStatic'
    DISCOUNTING = 'Discounting'
    VENDORDEFAULT = 'VendorDefault'
    BLACKSCHOLES = 'BlackScholes'
    CONSTANTTIMEVALUEOFMONEY = 'ConstantTimeValueOfMoney'
    BACHELIER = 'Bachelier'
    FORWARDWITHPOINTS = 'ForwardWithPoints'
    FORWARDWITHPOINTSUNDISCOUNTED = 'ForwardWithPointsUndiscounted'
    FORWARDSPECIFIEDRATE = 'ForwardSpecifiedRate'
    FORWARDSPECIFIEDRATEUNDISCOUNTED = 'ForwardSpecifiedRateUndiscounted'
    INDEXNAV = 'IndexNav'
    INDEXPRICE = 'IndexPrice'
    INLINEDINDEX = 'InlinedIndex'
    FORWARDFROMCURVE = 'ForwardFromCurve'
    FORWARDFROMCURVEUNDISCOUNTED = 'ForwardFromCurveUndiscounted'
    BLACKSCHOLESDIGITAL = 'BlackScholesDigital'
    BJERKSUNDSTENSLAND1993 = 'BjerksundStensland1993'
    BONDLOOKUPPRICER = 'BondLookupPricer'
    FLEXIBLELOANPRICER = 'FlexibleLoanPricer'
    CDSLOOKUPPRICER = 'CdsLookupPricer'
    LOANFACILITYPRICER = 'LoanFacilityPricer'

    @classmethod
    def from_json(cls, json_str: str) -> PricingModel:
        """Create an instance of PricingModel from a JSON string"""
        return PricingModel(json.loads(json_str))
