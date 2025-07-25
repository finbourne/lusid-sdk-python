# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    Contact: info@finbourne.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from typing import Any, Dict, List, Optional, Union
from pydantic.v1 import StrictStr, Field, Field, StrictFloat, StrictInt, StrictStr, conlist, constr, validator 
from lusid.models.lusid_instrument import LusidInstrument
from lusid.models.time_zone_conventions import TimeZoneConventions

class Repo(LusidInstrument):
    """
    LUSID representation of a sale and repurchase agreement, supporting haircut, margin or repo rate methods.  # noqa: E501
    """
    start_date: datetime = Field(..., alias="startDate", description="The start date of the instrument. This is normally synonymous with the trade-date.")
    maturity_date: datetime = Field(..., alias="maturityDate", description="The final maturity date of the instrument. This means the last date on which the instruments makes a payment of any amount.  For the avoidance of doubt, that is not necessarily prior to its last sensitivity date for the purposes of risk; e.g. instruments such as  Constant Maturity Swaps (CMS) often have sensitivities to rates that may well be observed or set prior to the maturity date, but refer to a termination date beyond it.")
    dom_ccy:  StrictStr = Field(...,alias="domCcy", description="The domestic currency of the instrument.") 
    accrual_basis:  StrictStr = Field(...,alias="accrualBasis", description="For calculation of interest, the accrual basis to be used.  For more information on day counts, see [knowledge base article KA-01798](https://support.lusid.com/knowledgebase/article/KA-01798)                Supported string (enumeration) values are: [Actual360, Act360, MoneyMarket, Actual365, Act365, Thirty360, ThirtyU360, Bond, ThirtyE360, EuroBond, ActualActual, ActAct, ActActIsda, ActActIsma, ActActIcma, OneOne, Act364, Act365F, Act365L, Act365_25, Act252, Bus252, NL360, NL365, ActActAFB, Act365Cad, ThirtyActIsda, Thirty365Isda, ThirtyEActIsda, ThirtyE360Isda, ThirtyE365Isda, ThirtyU360EOM].") 
    collateral: Optional[conlist(LusidInstrument)] = Field(None, description="The actual collateral in the Repo.  This property is for informational purposes only, Lusid pricing is not affected.")
    collateral_value: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="collateralValue", description="The full market value of the collateral in domestic currency, before any margin or haircut is applied.")
    haircut: Optional[Union[StrictFloat, StrictInt]] = Field(None, description="The haircut (or margin percentage) applied to the collateral, this should be a number between 0 and 1, i.e. for a 5% haircut this should be 0.05.  This is defined as (CollateralValue - PurchasePrice) / CollateralValue.  If this property is specified, so too must CollateralValue.  While this property is optional, one, and only one, of PurchasePrice, Margin and Haircut must be specified.")
    margin: Optional[Union[StrictFloat, StrictInt]] = Field(None, description="The initial margin (or margin ratio) applied to the collateral, this should be a number greater than or equal to 1.0,  i.e. for a 102% margin this should be 1.02. A value of 1.0 means no margin (100%).  This is defined as CollateralValue / PurchasePrice.  If this property is specified, so too must CollateralValue.  While this property is optional, one, and only one, of PurchasePrice, Margin and Haircut must be specified.")
    purchase_price: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="purchasePrice", description="The price the collateral is initially purchased for, this property can be used to explicitly set the purchase price and not require  collateral value and a margin or haircut.  While this property is optional, one, and only one, of PurchasePrice, Margin and Haircut must be specified.")
    repo_rate: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="repoRate", description="The rate at which interest is to be accrue and be paid upon redemption of the collateral at maturity.  This field is used to calculate the Repurchase price.  While this property is optional, one, and only one, of the RepoRate and RepurchasePrice must be specified.")
    repurchase_price: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="repurchasePrice", description="The price at which the collateral is repurchased, this field is optional and can be explicitly set here or will be calculated  from the PurchasePrice and RepoRate.  One, and only one, of the RepoRate and RepurchasePrice must be specified.")
    time_zone_conventions: Optional[TimeZoneConventions] = Field(None, alias="timeZoneConventions")
    instrument_type:  StrictStr = Field(...,alias="instrumentType", description="The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap, SimpleCashFlowLoan, TotalReturnSwap, InflationLeg, FundShareClass, FlexibleLoan, UnsettledCash, Cash, MasteredInstrument, LoanFacility, FlexibleDeposit, FlexibleRepo") 
    additional_properties: Dict[str, Any] = {}
    __properties = ["instrumentType", "startDate", "maturityDate", "domCcy", "accrualBasis", "collateral", "collateralValue", "haircut", "margin", "purchasePrice", "repoRate", "repurchasePrice", "timeZoneConventions"]

    @validator('instrument_type')
    def instrument_type_validate_enum(cls, value):
        """Validates the enum"""

        # Finbourne have removed enum validation on all models, except for this use case:
        # Workflow and notification application SDK use the property name 'type' as the discriminator on a number of classes.
        # During instantiation, the value of 'type' is checked against the enum values, 
        

        # check it's a class that uses the 'type' property as a discriminator
        # list of classes can be found by searching for 'actual_instance: Union[' in the generated code
        if 'Repo' not in [ 
                                    # For notification application classes
                                    'AmazonSqsNotificationType',
                                    'AmazonSqsNotificationTypeResponse',
                                    'AmazonSqsPrincipalAuthNotificationType',
                                    'AmazonSqsPrincipalAuthNotificationTypeResponse',
                                    'AzureServiceBusTypeResponse',
                                    'AzureServiceBusNotificationType',
                                    'EmailNotificationType',
                                    'EmailNotificationTypeResponse',
                                    'SmsNotificationType',
                                    'SmsNotificationTypeResponse',
                                    'WebhookNotificationType',
                                    'WebhookNotificationTypeResponse',
                        
                                    # For workflow application classes
                                    'CreateChildTasksAction', 
                                    'RunWorkerAction', 
                                    'TriggerParentTaskAction',
                                    'CreateChildTasksActionResponse', 
                                    'RunWorkerActionResponse',
                                    'TriggerParentTaskActionResponse',
                                    'CreateNewTaskActivity',
                                    'UpdateMatchingTasksActivity',
                                    'CreateNewTaskActivityResponse', 
                                    'UpdateMatchingTasksActivityResponse',
                                    'Fail', 
                                    'GroupReconciliation', 
                                    'HealthCheck', 
                                    'LuminesceView', 
                                    'SchedulerJob', 
                                    'Sleep',
                                    'FailResponse', 
                                    'GroupReconciliationResponse', 
                                    'HealthCheckResponse', 
                                    'LuminesceViewResponse', 
                                    'SchedulerJobResponse', 
                                    'SleepResponse']:
           return value
        
        # Only validate the 'type' property of the class
        if "instrument_type" != "type":
            return value

        if value not in ('QuotedSecurity', 'InterestRateSwap', 'FxForward', 'Future', 'ExoticInstrument', 'FxOption', 'CreditDefaultSwap', 'InterestRateSwaption', 'Bond', 'EquityOption', 'FixedLeg', 'FloatingLeg', 'BespokeCashFlowsLeg', 'Unknown', 'TermDeposit', 'ContractForDifference', 'EquitySwap', 'CashPerpetual', 'CapFloor', 'CashSettled', 'CdsIndex', 'Basket', 'FundingLeg', 'FxSwap', 'ForwardRateAgreement', 'SimpleInstrument', 'Repo', 'Equity', 'ExchangeTradedOption', 'ReferenceInstrument', 'ComplexBond', 'InflationLinkedBond', 'InflationSwap', 'SimpleCashFlowLoan', 'TotalReturnSwap', 'InflationLeg', 'FundShareClass', 'FlexibleLoan', 'UnsettledCash', 'Cash', 'MasteredInstrument', 'LoanFacility', 'FlexibleDeposit', 'FlexibleRepo'):
            raise ValueError("must be one of enum values ('QuotedSecurity', 'InterestRateSwap', 'FxForward', 'Future', 'ExoticInstrument', 'FxOption', 'CreditDefaultSwap', 'InterestRateSwaption', 'Bond', 'EquityOption', 'FixedLeg', 'FloatingLeg', 'BespokeCashFlowsLeg', 'Unknown', 'TermDeposit', 'ContractForDifference', 'EquitySwap', 'CashPerpetual', 'CapFloor', 'CashSettled', 'CdsIndex', 'Basket', 'FundingLeg', 'FxSwap', 'ForwardRateAgreement', 'SimpleInstrument', 'Repo', 'Equity', 'ExchangeTradedOption', 'ReferenceInstrument', 'ComplexBond', 'InflationLinkedBond', 'InflationSwap', 'SimpleCashFlowLoan', 'TotalReturnSwap', 'InflationLeg', 'FundShareClass', 'FlexibleLoan', 'UnsettledCash', 'Cash', 'MasteredInstrument', 'LoanFacility', 'FlexibleDeposit', 'FlexibleRepo')")
        return value

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def __str__(self):
        """For `print` and `pprint`"""
        return pprint.pformat(self.dict(by_alias=False))

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Repo:
        """Create an instance of Repo from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "additional_properties"
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in collateral (list)
        _items = []
        if self.collateral:
            for _item in self.collateral:
                if _item:
                    _items.append(_item.to_dict())
            _dict['collateral'] = _items
        # override the default output from pydantic by calling `to_dict()` of time_zone_conventions
        if self.time_zone_conventions:
            _dict['timeZoneConventions'] = self.time_zone_conventions.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        # set to None if collateral (nullable) is None
        # and __fields_set__ contains the field
        if self.collateral is None and "collateral" in self.__fields_set__:
            _dict['collateral'] = None

        # set to None if collateral_value (nullable) is None
        # and __fields_set__ contains the field
        if self.collateral_value is None and "collateral_value" in self.__fields_set__:
            _dict['collateralValue'] = None

        # set to None if haircut (nullable) is None
        # and __fields_set__ contains the field
        if self.haircut is None and "haircut" in self.__fields_set__:
            _dict['haircut'] = None

        # set to None if margin (nullable) is None
        # and __fields_set__ contains the field
        if self.margin is None and "margin" in self.__fields_set__:
            _dict['margin'] = None

        # set to None if purchase_price (nullable) is None
        # and __fields_set__ contains the field
        if self.purchase_price is None and "purchase_price" in self.__fields_set__:
            _dict['purchasePrice'] = None

        # set to None if repo_rate (nullable) is None
        # and __fields_set__ contains the field
        if self.repo_rate is None and "repo_rate" in self.__fields_set__:
            _dict['repoRate'] = None

        # set to None if repurchase_price (nullable) is None
        # and __fields_set__ contains the field
        if self.repurchase_price is None and "repurchase_price" in self.__fields_set__:
            _dict['repurchasePrice'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Repo:
        """Create an instance of Repo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Repo.parse_obj(obj)

        _obj = Repo.parse_obj({
            "instrument_type": obj.get("instrumentType"),
            "start_date": obj.get("startDate"),
            "maturity_date": obj.get("maturityDate"),
            "dom_ccy": obj.get("domCcy"),
            "accrual_basis": obj.get("accrualBasis"),
            "collateral": [LusidInstrument.from_dict(_item) for _item in obj.get("collateral")] if obj.get("collateral") is not None else None,
            "collateral_value": obj.get("collateralValue"),
            "haircut": obj.get("haircut"),
            "margin": obj.get("margin"),
            "purchase_price": obj.get("purchasePrice"),
            "repo_rate": obj.get("repoRate"),
            "repurchase_price": obj.get("repurchasePrice"),
            "time_zone_conventions": TimeZoneConventions.from_dict(obj.get("timeZoneConventions")) if obj.get("timeZoneConventions") is not None else None
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj
