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
from pydantic.v1 import StrictStr, Field, BaseModel, Field, StrictFloat, StrictInt, StrictStr, conlist, constr, validator 
from lusid.models.currency_and_amount import CurrencyAndAmount
from lusid.models.custodian_account import CustodianAccount
from lusid.models.economics import Economics
from lusid.models.otc_confirmation import OtcConfirmation
from lusid.models.perpetual_property import PerpetualProperty
from lusid.models.realised_gain_loss import RealisedGainLoss
from lusid.models.resource_id import ResourceId
from lusid.models.transaction_price import TransactionPrice
from lusid.models.transaction_type_details import TransactionTypeDetails

class OutputTransaction(BaseModel):
    """
    A list of output transactions.  # noqa: E501
    """
    transaction_id:  StrictStr = Field(...,alias="transactionId", description="The unique identifier for the transaction.") 
    type:  StrictStr = Field(...,alias="type", description="The type of the transaction e.g. 'Buy', 'Sell'. The transaction type should have been pre-configured via the System Configuration API endpoint.") 
    description:  Optional[StrictStr] = Field(None,alias="description", description="The description of the transaction. This only exists on transactions generated by LUSID e.g. a holdings adjustment transaction.") 
    instrument_identifiers: Optional[Dict[str, StrictStr]] = Field(None, alias="instrumentIdentifiers", description="A set of instrument identifiers that can resolve the transaction to a unique instrument.")
    instrument_scope:  Optional[StrictStr] = Field(None,alias="instrumentScope", description="The scope in which the instrument lies.") 
    instrument_uid:  StrictStr = Field(...,alias="instrumentUid", description="The unique Lusid Instrument Id (LUID) of the instrument that the transaction is in.") 
    transaction_date: datetime = Field(..., alias="transactionDate", description="The date of the transaction.")
    settlement_date: datetime = Field(..., alias="settlementDate", description="The settlement date of the transaction.")
    units: Union[StrictFloat, StrictInt] = Field(..., description="The number of units transacted in the associated instrument.")
    transaction_amount: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="transactionAmount", description="The total value of the transaction in the transaction currency.")
    transaction_price: Optional[TransactionPrice] = Field(None, alias="transactionPrice")
    total_consideration: Optional[CurrencyAndAmount] = Field(None, alias="totalConsideration")
    exchange_rate: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="exchangeRate", description="The exchange rate between the transaction and settlement currency (settlement currency being represented by the TotalConsideration.Currency). For example if the transaction currency is in USD and the settlement currency is in GBP this this the USD/GBP rate.")
    transaction_to_portfolio_rate: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="transactionToPortfolioRate", description="The exchange rate between the transaction and portfolio currency. For example if the transaction currency is in USD and the portfolio currency is in GBP this this the USD/GBP rate.")
    transaction_currency:  Optional[StrictStr] = Field(None,alias="transactionCurrency", description="The transaction currency.") 
    properties: Optional[Dict[str, PerpetualProperty]] = Field(None, description="Set of unique transaction properties and associated values to stored with the transaction. Each property will be from the 'Transaction' domain.")
    counterparty_id:  Optional[StrictStr] = Field(None,alias="counterpartyId", description="The identifier for the counterparty of the transaction.") 
    source:  Optional[StrictStr] = Field(None,alias="source", description="The source of the transaction. This is used to look up the appropriate transaction group set in the transaction type configuration.") 
    transaction_status:  Optional[StrictStr] = Field(None,alias="transactionStatus", description="The status of the transaction. The available values are: Active, Amended, Cancelled, ActiveReversal, ActiveTrueUp, CancelledTrueUp") 
    entry_date_time: Optional[datetime] = Field(None, alias="entryDateTime", description="The asAt datetime that the transaction was added to LUSID.")
    cancel_date_time: Optional[datetime] = Field(None, alias="cancelDateTime", description="If the transaction has been cancelled, the asAt datetime that the transaction was cancelled.")
    realised_gain_loss: Optional[conlist(RealisedGainLoss)] = Field(None, alias="realisedGainLoss", description="The collection of realised gains or losses resulting from relevant transactions e.g. a sale transaction. The cost used in calculating the realised gain or loss is determined by the accounting method defined when the transaction portfolio is created.")
    holding_ids: Optional[conlist(StrictInt)] = Field(None, alias="holdingIds", description="The collection of single identifiers for the holding within the portfolio. The holdingId is constructed from the LusidInstrumentId, sub-holding keys and currrency and is unique within the portfolio.")
    source_type:  Optional[StrictStr] = Field(None,alias="sourceType", description="The type of source that the transaction originated from, eg: InputTransaction, InstrumentEvent, HoldingAdjustment") 
    source_instrument_event_id:  Optional[StrictStr] = Field(None,alias="sourceInstrumentEventId", description="The unique ID of the instrument event that the transaction is related to.") 
    custodian_account: Optional[CustodianAccount] = Field(None, alias="custodianAccount")
    transaction_group_id:  Optional[StrictStr] = Field(None,alias="transactionGroupId", description="The identifier for grouping economic events across multiple transactions") 
    resolved_transaction_type_details: Optional[TransactionTypeDetails] = Field(None, alias="resolvedTransactionTypeDetails")
    gross_transaction_amount: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="grossTransactionAmount", description="The total gross value of the transaction in the transaction currency.")
    otc_confirmation: Optional[OtcConfirmation] = Field(None, alias="otcConfirmation")
    order_id: Optional[ResourceId] = Field(None, alias="orderId")
    allocation_id: Optional[ResourceId] = Field(None, alias="allocationId")
    accounting_date: Optional[datetime] = Field(None, alias="accountingDate", description="The accounting date of the transaction.")
    economics: Optional[conlist(Economics)] = Field(None, description="Set of economic data related with the transaction impacts.")
    __properties = ["transactionId", "type", "description", "instrumentIdentifiers", "instrumentScope", "instrumentUid", "transactionDate", "settlementDate", "units", "transactionAmount", "transactionPrice", "totalConsideration", "exchangeRate", "transactionToPortfolioRate", "transactionCurrency", "properties", "counterpartyId", "source", "transactionStatus", "entryDateTime", "cancelDateTime", "realisedGainLoss", "holdingIds", "sourceType", "sourceInstrumentEventId", "custodianAccount", "transactionGroupId", "resolvedTransactionTypeDetails", "grossTransactionAmount", "otcConfirmation", "orderId", "allocationId", "accountingDate", "economics"]

    @validator('transaction_status')
    def transaction_status_validate_enum(cls, value):
        """Validates the enum"""

        # Finbourne have removed enum validation on all models, except for this use case:
        # Workflow and notification application SDK use the property name 'type' as the discriminator on a number of classes.
        # During instantiation, the value of 'type' is checked against the enum values, 
        

        # check it's a class that uses the 'type' property as a discriminator
        # list of classes can be found by searching for 'actual_instance: Union[' in the generated code
        if 'OutputTransaction' not in [ 
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
        if "transaction_status" != "type":
            return value

        if value is None:
            return value

        if value not in ('Active', 'Amended', 'Cancelled', 'ActiveReversal', 'ActiveTrueUp', 'CancelledTrueUp'):
            raise ValueError("must be one of enum values ('Active', 'Amended', 'Cancelled', 'ActiveReversal', 'ActiveTrueUp', 'CancelledTrueUp')")
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
    def from_json(cls, json_str: str) -> OutputTransaction:
        """Create an instance of OutputTransaction from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of transaction_price
        if self.transaction_price:
            _dict['transactionPrice'] = self.transaction_price.to_dict()
        # override the default output from pydantic by calling `to_dict()` of total_consideration
        if self.total_consideration:
            _dict['totalConsideration'] = self.total_consideration.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each value in properties (dict)
        _field_dict = {}
        if self.properties:
            for _key in self.properties:
                if self.properties[_key]:
                    _field_dict[_key] = self.properties[_key].to_dict()
            _dict['properties'] = _field_dict
        # override the default output from pydantic by calling `to_dict()` of each item in realised_gain_loss (list)
        _items = []
        if self.realised_gain_loss:
            for _item in self.realised_gain_loss:
                if _item:
                    _items.append(_item.to_dict())
            _dict['realisedGainLoss'] = _items
        # override the default output from pydantic by calling `to_dict()` of custodian_account
        if self.custodian_account:
            _dict['custodianAccount'] = self.custodian_account.to_dict()
        # override the default output from pydantic by calling `to_dict()` of resolved_transaction_type_details
        if self.resolved_transaction_type_details:
            _dict['resolvedTransactionTypeDetails'] = self.resolved_transaction_type_details.to_dict()
        # override the default output from pydantic by calling `to_dict()` of otc_confirmation
        if self.otc_confirmation:
            _dict['otcConfirmation'] = self.otc_confirmation.to_dict()
        # override the default output from pydantic by calling `to_dict()` of order_id
        if self.order_id:
            _dict['orderId'] = self.order_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of allocation_id
        if self.allocation_id:
            _dict['allocationId'] = self.allocation_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in economics (list)
        _items = []
        if self.economics:
            for _item in self.economics:
                if _item:
                    _items.append(_item.to_dict())
            _dict['economics'] = _items
        # set to None if description (nullable) is None
        # and __fields_set__ contains the field
        if self.description is None and "description" in self.__fields_set__:
            _dict['description'] = None

        # set to None if instrument_identifiers (nullable) is None
        # and __fields_set__ contains the field
        if self.instrument_identifiers is None and "instrument_identifiers" in self.__fields_set__:
            _dict['instrumentIdentifiers'] = None

        # set to None if instrument_scope (nullable) is None
        # and __fields_set__ contains the field
        if self.instrument_scope is None and "instrument_scope" in self.__fields_set__:
            _dict['instrumentScope'] = None

        # set to None if transaction_to_portfolio_rate (nullable) is None
        # and __fields_set__ contains the field
        if self.transaction_to_portfolio_rate is None and "transaction_to_portfolio_rate" in self.__fields_set__:
            _dict['transactionToPortfolioRate'] = None

        # set to None if transaction_currency (nullable) is None
        # and __fields_set__ contains the field
        if self.transaction_currency is None and "transaction_currency" in self.__fields_set__:
            _dict['transactionCurrency'] = None

        # set to None if properties (nullable) is None
        # and __fields_set__ contains the field
        if self.properties is None and "properties" in self.__fields_set__:
            _dict['properties'] = None

        # set to None if counterparty_id (nullable) is None
        # and __fields_set__ contains the field
        if self.counterparty_id is None and "counterparty_id" in self.__fields_set__:
            _dict['counterpartyId'] = None

        # set to None if source (nullable) is None
        # and __fields_set__ contains the field
        if self.source is None and "source" in self.__fields_set__:
            _dict['source'] = None

        # set to None if cancel_date_time (nullable) is None
        # and __fields_set__ contains the field
        if self.cancel_date_time is None and "cancel_date_time" in self.__fields_set__:
            _dict['cancelDateTime'] = None

        # set to None if realised_gain_loss (nullable) is None
        # and __fields_set__ contains the field
        if self.realised_gain_loss is None and "realised_gain_loss" in self.__fields_set__:
            _dict['realisedGainLoss'] = None

        # set to None if holding_ids (nullable) is None
        # and __fields_set__ contains the field
        if self.holding_ids is None and "holding_ids" in self.__fields_set__:
            _dict['holdingIds'] = None

        # set to None if source_type (nullable) is None
        # and __fields_set__ contains the field
        if self.source_type is None and "source_type" in self.__fields_set__:
            _dict['sourceType'] = None

        # set to None if source_instrument_event_id (nullable) is None
        # and __fields_set__ contains the field
        if self.source_instrument_event_id is None and "source_instrument_event_id" in self.__fields_set__:
            _dict['sourceInstrumentEventId'] = None

        # set to None if transaction_group_id (nullable) is None
        # and __fields_set__ contains the field
        if self.transaction_group_id is None and "transaction_group_id" in self.__fields_set__:
            _dict['transactionGroupId'] = None

        # set to None if accounting_date (nullable) is None
        # and __fields_set__ contains the field
        if self.accounting_date is None and "accounting_date" in self.__fields_set__:
            _dict['accountingDate'] = None

        # set to None if economics (nullable) is None
        # and __fields_set__ contains the field
        if self.economics is None and "economics" in self.__fields_set__:
            _dict['economics'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> OutputTransaction:
        """Create an instance of OutputTransaction from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return OutputTransaction.parse_obj(obj)

        _obj = OutputTransaction.parse_obj({
            "transaction_id": obj.get("transactionId"),
            "type": obj.get("type"),
            "description": obj.get("description"),
            "instrument_identifiers": obj.get("instrumentIdentifiers"),
            "instrument_scope": obj.get("instrumentScope"),
            "instrument_uid": obj.get("instrumentUid"),
            "transaction_date": obj.get("transactionDate"),
            "settlement_date": obj.get("settlementDate"),
            "units": obj.get("units"),
            "transaction_amount": obj.get("transactionAmount"),
            "transaction_price": TransactionPrice.from_dict(obj.get("transactionPrice")) if obj.get("transactionPrice") is not None else None,
            "total_consideration": CurrencyAndAmount.from_dict(obj.get("totalConsideration")) if obj.get("totalConsideration") is not None else None,
            "exchange_rate": obj.get("exchangeRate"),
            "transaction_to_portfolio_rate": obj.get("transactionToPortfolioRate"),
            "transaction_currency": obj.get("transactionCurrency"),
            "properties": dict(
                (_k, PerpetualProperty.from_dict(_v))
                for _k, _v in obj.get("properties").items()
            )
            if obj.get("properties") is not None
            else None,
            "counterparty_id": obj.get("counterpartyId"),
            "source": obj.get("source"),
            "transaction_status": obj.get("transactionStatus"),
            "entry_date_time": obj.get("entryDateTime"),
            "cancel_date_time": obj.get("cancelDateTime"),
            "realised_gain_loss": [RealisedGainLoss.from_dict(_item) for _item in obj.get("realisedGainLoss")] if obj.get("realisedGainLoss") is not None else None,
            "holding_ids": obj.get("holdingIds"),
            "source_type": obj.get("sourceType"),
            "source_instrument_event_id": obj.get("sourceInstrumentEventId"),
            "custodian_account": CustodianAccount.from_dict(obj.get("custodianAccount")) if obj.get("custodianAccount") is not None else None,
            "transaction_group_id": obj.get("transactionGroupId"),
            "resolved_transaction_type_details": TransactionTypeDetails.from_dict(obj.get("resolvedTransactionTypeDetails")) if obj.get("resolvedTransactionTypeDetails") is not None else None,
            "gross_transaction_amount": obj.get("grossTransactionAmount"),
            "otc_confirmation": OtcConfirmation.from_dict(obj.get("otcConfirmation")) if obj.get("otcConfirmation") is not None else None,
            "order_id": ResourceId.from_dict(obj.get("orderId")) if obj.get("orderId") is not None else None,
            "allocation_id": ResourceId.from_dict(obj.get("allocationId")) if obj.get("allocationId") is not None else None,
            "accounting_date": obj.get("accountingDate"),
            "economics": [Economics.from_dict(_item) for _item in obj.get("economics")] if obj.get("economics") is not None else None
        })
        return _obj
