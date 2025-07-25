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


from typing import Any, Dict, List, Optional
from pydantic.v1 import StrictStr, Field, BaseModel, Field, StrictBool, StrictStr, conlist, validator 
from lusid.models.link import Link
from lusid.models.resource_id import ResourceId

class PropertyDefinitionSearchResult(BaseModel):
    """
    A property definition search result  # noqa: E501
    """
    href:  Optional[StrictStr] = Field(None,alias="href", description="The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.") 
    key:  Optional[StrictStr] = Field(None,alias="key", description="The property key which uniquely identifies the property. The format for the property key is {domain}/{scope}/{code}, e.g. 'Portfolio/Manager/Id'.") 
    value_type:  Optional[StrictStr] = Field(None,alias="valueType", description="The type of values that can be associated with this property. This is defined by the property's data type. The available values are: String, Int, Decimal, DateTime, Boolean, Map, List, PropertyArray, Percentage, Code, Id, Uri, CurrencyAndAmount, TradePrice, Currency, MetricValue, ResourceId, ResultValue, CutLocalTime, DateOrCutLabel, UnindexedText") 
    display_name:  Optional[StrictStr] = Field(None,alias="displayName", description="The display name of the property.") 
    data_type_id: Optional[ResourceId] = Field(None, alias="dataTypeId")
    type:  Optional[StrictStr] = Field(None,alias="type", description="The type of the property. The available values are: Label, Metric, Information") 
    unit_schema:  Optional[StrictStr] = Field(None,alias="unitSchema", description="The units that can be associated with the property's values. This is defined by the property's data type. The available values are: NoUnits, Basic, Iso4217Currency") 
    domain:  Optional[StrictStr] = Field(None,alias="domain", description="The domain that the property exists in. The available values are: NotDefined, Transaction, Portfolio, Holding, ReferenceHolding, TransactionConfiguration, Instrument, CutLabelDefinition, Analytic, PortfolioGroup, Person, AccessMetadata, Order, UnitResult, MarketData, ConfigurationRecipe, Allocation, Calendar, LegalEntity, InvestorRecord, InvestmentAccount, Placement, Execution, Block, Participation, Package, OrderInstruction, NextBestAction, CustomEntity, InstrumentEvent, Account, ChartOfAccounts, CustodianAccount, CheckDefinition, Abor, AborConfiguration, Fund, FundConfiguration, Fee, Reconciliation, PropertyDefinition, Compliance, DiaryEntry, Leg, DerivedValuation, Timeline, ClosedPeriod, AddressKeyDefinition, AmortisationRuleSet, AnalyticsSetInventory, AtomUnitResult, CleardownModule, ComplexMarketData, ComplianceRunSummary, ComplianceRule, ComplianceRunInfo, CorporateActionSource, CounterpartyAgreement, CustomEntityDefinition, DataType, Dialect, EventHandler, GeneralLedgerProfile, PostingModule, Quote, RecipeComposer, ReconciliationRunBreak, ReferenceList, RelationDefinition, ReturnBlockIndex, SRSDocument, SRSIndex, TransactionTemplate, TransactionTemplateScope, TransactionType, TransactionTypeConfig, TranslationScript, TaskDefinition, TaskInstance, Worker, StagingRuleSet, IdentifierDefinition") 
    scope:  Optional[StrictStr] = Field(None,alias="scope", description="The scope that the property exists in.") 
    code:  Optional[StrictStr] = Field(None,alias="code", description="The code of the property. Together with the domain and scope this uniquely identifies the property.") 
    value_required: Optional[StrictBool] = Field(None, alias="valueRequired", description="This field is not implemented and should be disregarded.")
    life_time:  Optional[StrictStr] = Field(None,alias="lifeTime", description="Describes how the property's values can change over time. The available values are: Perpetual, TimeVariant") 
    constraint_style:  Optional[StrictStr] = Field(None,alias="constraintStyle", description="Describes the uniqueness and cardinality of the property for entity objects under the property domain specified in Key.") 
    property_definition_type:  Optional[StrictStr] = Field(None,alias="propertyDefinitionType", description="The definition type (DerivedDefinition or Definition). The available values are: ValueProperty, DerivedDefinition") 
    property_description:  Optional[StrictStr] = Field(None,alias="propertyDescription", description="A brief description of what a property of this property definition contains.") 
    derivation_formula:  Optional[StrictStr] = Field(None,alias="derivationFormula", description="The rule that defines how data is composed for a derived property.") 
    is_filterable: Optional[StrictBool] = Field(None, alias="isFilterable", description="Bool indicating whether the values of this property are fitlerable, this is true for all non-derived property defintions.  For a derived definition this must be set true to enable filtering.")
    links: Optional[conlist(Link)] = None
    __properties = ["href", "key", "valueType", "displayName", "dataTypeId", "type", "unitSchema", "domain", "scope", "code", "valueRequired", "lifeTime", "constraintStyle", "propertyDefinitionType", "propertyDescription", "derivationFormula", "isFilterable", "links"]

    @validator('value_type')
    def value_type_validate_enum(cls, value):
        """Validates the enum"""

        # Finbourne have removed enum validation on all models, except for this use case:
        # Workflow and notification application SDK use the property name 'type' as the discriminator on a number of classes.
        # During instantiation, the value of 'type' is checked against the enum values, 
        

        # check it's a class that uses the 'type' property as a discriminator
        # list of classes can be found by searching for 'actual_instance: Union[' in the generated code
        if 'PropertyDefinitionSearchResult' not in [ 
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
        if "value_type" != "type":
            return value

        if value is None:
            return value

        if value not in ('String', 'Int', 'Decimal', 'DateTime', 'Boolean', 'Map', 'List', 'PropertyArray', 'Percentage', 'Code', 'Id', 'Uri', 'CurrencyAndAmount', 'TradePrice', 'Currency', 'MetricValue', 'ResourceId', 'ResultValue', 'CutLocalTime', 'DateOrCutLabel', 'UnindexedText'):
            raise ValueError("must be one of enum values ('String', 'Int', 'Decimal', 'DateTime', 'Boolean', 'Map', 'List', 'PropertyArray', 'Percentage', 'Code', 'Id', 'Uri', 'CurrencyAndAmount', 'TradePrice', 'Currency', 'MetricValue', 'ResourceId', 'ResultValue', 'CutLocalTime', 'DateOrCutLabel', 'UnindexedText')")
        return value

    @validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""

        # Finbourne have removed enum validation on all models, except for this use case:
        # Workflow and notification application SDK use the property name 'type' as the discriminator on a number of classes.
        # During instantiation, the value of 'type' is checked against the enum values, 
        

        # check it's a class that uses the 'type' property as a discriminator
        # list of classes can be found by searching for 'actual_instance: Union[' in the generated code
        if 'PropertyDefinitionSearchResult' not in [ 
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
        if "type" != "type":
            return value

        if value is None:
            return value

        if value not in ('Label', 'Metric', 'Information'):
            raise ValueError("must be one of enum values ('Label', 'Metric', 'Information')")
        return value

    @validator('unit_schema')
    def unit_schema_validate_enum(cls, value):
        """Validates the enum"""

        # Finbourne have removed enum validation on all models, except for this use case:
        # Workflow and notification application SDK use the property name 'type' as the discriminator on a number of classes.
        # During instantiation, the value of 'type' is checked against the enum values, 
        

        # check it's a class that uses the 'type' property as a discriminator
        # list of classes can be found by searching for 'actual_instance: Union[' in the generated code
        if 'PropertyDefinitionSearchResult' not in [ 
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
        if "unit_schema" != "type":
            return value

        if value is None:
            return value

        if value not in ('NoUnits', 'Basic', 'Iso4217Currency'):
            raise ValueError("must be one of enum values ('NoUnits', 'Basic', 'Iso4217Currency')")
        return value

    @validator('domain')
    def domain_validate_enum(cls, value):
        """Validates the enum"""

        # Finbourne have removed enum validation on all models, except for this use case:
        # Workflow and notification application SDK use the property name 'type' as the discriminator on a number of classes.
        # During instantiation, the value of 'type' is checked against the enum values, 
        

        # check it's a class that uses the 'type' property as a discriminator
        # list of classes can be found by searching for 'actual_instance: Union[' in the generated code
        if 'PropertyDefinitionSearchResult' not in [ 
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
        if "domain" != "type":
            return value

        if value is None:
            return value

        if value not in ('NotDefined', 'Transaction', 'Portfolio', 'Holding', 'ReferenceHolding', 'TransactionConfiguration', 'Instrument', 'CutLabelDefinition', 'Analytic', 'PortfolioGroup', 'Person', 'AccessMetadata', 'Order', 'UnitResult', 'MarketData', 'ConfigurationRecipe', 'Allocation', 'Calendar', 'LegalEntity', 'InvestorRecord', 'InvestmentAccount', 'Placement', 'Execution', 'Block', 'Participation', 'Package', 'OrderInstruction', 'NextBestAction', 'CustomEntity', 'InstrumentEvent', 'Account', 'ChartOfAccounts', 'CustodianAccount', 'CheckDefinition', 'Abor', 'AborConfiguration', 'Fund', 'FundConfiguration', 'Fee', 'Reconciliation', 'PropertyDefinition', 'Compliance', 'DiaryEntry', 'Leg', 'DerivedValuation', 'Timeline', 'ClosedPeriod', 'AddressKeyDefinition', 'AmortisationRuleSet', 'AnalyticsSetInventory', 'AtomUnitResult', 'CleardownModule', 'ComplexMarketData', 'ComplianceRunSummary', 'ComplianceRule', 'ComplianceRunInfo', 'CorporateActionSource', 'CounterpartyAgreement', 'CustomEntityDefinition', 'DataType', 'Dialect', 'EventHandler', 'GeneralLedgerProfile', 'PostingModule', 'Quote', 'RecipeComposer', 'ReconciliationRunBreak', 'ReferenceList', 'RelationDefinition', 'ReturnBlockIndex', 'SRSDocument', 'SRSIndex', 'TransactionTemplate', 'TransactionTemplateScope', 'TransactionType', 'TransactionTypeConfig', 'TranslationScript', 'TaskDefinition', 'TaskInstance', 'Worker', 'StagingRuleSet', 'IdentifierDefinition'):
            raise ValueError("must be one of enum values ('NotDefined', 'Transaction', 'Portfolio', 'Holding', 'ReferenceHolding', 'TransactionConfiguration', 'Instrument', 'CutLabelDefinition', 'Analytic', 'PortfolioGroup', 'Person', 'AccessMetadata', 'Order', 'UnitResult', 'MarketData', 'ConfigurationRecipe', 'Allocation', 'Calendar', 'LegalEntity', 'InvestorRecord', 'InvestmentAccount', 'Placement', 'Execution', 'Block', 'Participation', 'Package', 'OrderInstruction', 'NextBestAction', 'CustomEntity', 'InstrumentEvent', 'Account', 'ChartOfAccounts', 'CustodianAccount', 'CheckDefinition', 'Abor', 'AborConfiguration', 'Fund', 'FundConfiguration', 'Fee', 'Reconciliation', 'PropertyDefinition', 'Compliance', 'DiaryEntry', 'Leg', 'DerivedValuation', 'Timeline', 'ClosedPeriod', 'AddressKeyDefinition', 'AmortisationRuleSet', 'AnalyticsSetInventory', 'AtomUnitResult', 'CleardownModule', 'ComplexMarketData', 'ComplianceRunSummary', 'ComplianceRule', 'ComplianceRunInfo', 'CorporateActionSource', 'CounterpartyAgreement', 'CustomEntityDefinition', 'DataType', 'Dialect', 'EventHandler', 'GeneralLedgerProfile', 'PostingModule', 'Quote', 'RecipeComposer', 'ReconciliationRunBreak', 'ReferenceList', 'RelationDefinition', 'ReturnBlockIndex', 'SRSDocument', 'SRSIndex', 'TransactionTemplate', 'TransactionTemplateScope', 'TransactionType', 'TransactionTypeConfig', 'TranslationScript', 'TaskDefinition', 'TaskInstance', 'Worker', 'StagingRuleSet', 'IdentifierDefinition')")
        return value

    @validator('life_time')
    def life_time_validate_enum(cls, value):
        """Validates the enum"""

        # Finbourne have removed enum validation on all models, except for this use case:
        # Workflow and notification application SDK use the property name 'type' as the discriminator on a number of classes.
        # During instantiation, the value of 'type' is checked against the enum values, 
        

        # check it's a class that uses the 'type' property as a discriminator
        # list of classes can be found by searching for 'actual_instance: Union[' in the generated code
        if 'PropertyDefinitionSearchResult' not in [ 
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
        if "life_time" != "type":
            return value

        if value is None:
            return value

        if value not in ('Perpetual', 'TimeVariant'):
            raise ValueError("must be one of enum values ('Perpetual', 'TimeVariant')")
        return value

    @validator('property_definition_type')
    def property_definition_type_validate_enum(cls, value):
        """Validates the enum"""

        # Finbourne have removed enum validation on all models, except for this use case:
        # Workflow and notification application SDK use the property name 'type' as the discriminator on a number of classes.
        # During instantiation, the value of 'type' is checked against the enum values, 
        

        # check it's a class that uses the 'type' property as a discriminator
        # list of classes can be found by searching for 'actual_instance: Union[' in the generated code
        if 'PropertyDefinitionSearchResult' not in [ 
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
        if "property_definition_type" != "type":
            return value

        if value is None:
            return value

        if value not in ('ValueProperty', 'DerivedDefinition'):
            raise ValueError("must be one of enum values ('ValueProperty', 'DerivedDefinition')")
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
    def from_json(cls, json_str: str) -> PropertyDefinitionSearchResult:
        """Create an instance of PropertyDefinitionSearchResult from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "scope",
                            "code",
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of data_type_id
        if self.data_type_id:
            _dict['dataTypeId'] = self.data_type_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in links (list)
        _items = []
        if self.links:
            for _item in self.links:
                if _item:
                    _items.append(_item.to_dict())
            _dict['links'] = _items
        # set to None if href (nullable) is None
        # and __fields_set__ contains the field
        if self.href is None and "href" in self.__fields_set__:
            _dict['href'] = None

        # set to None if key (nullable) is None
        # and __fields_set__ contains the field
        if self.key is None and "key" in self.__fields_set__:
            _dict['key'] = None

        # set to None if display_name (nullable) is None
        # and __fields_set__ contains the field
        if self.display_name is None and "display_name" in self.__fields_set__:
            _dict['displayName'] = None

        # set to None if scope (nullable) is None
        # and __fields_set__ contains the field
        if self.scope is None and "scope" in self.__fields_set__:
            _dict['scope'] = None

        # set to None if code (nullable) is None
        # and __fields_set__ contains the field
        if self.code is None and "code" in self.__fields_set__:
            _dict['code'] = None

        # set to None if constraint_style (nullable) is None
        # and __fields_set__ contains the field
        if self.constraint_style is None and "constraint_style" in self.__fields_set__:
            _dict['constraintStyle'] = None

        # set to None if property_description (nullable) is None
        # and __fields_set__ contains the field
        if self.property_description is None and "property_description" in self.__fields_set__:
            _dict['propertyDescription'] = None

        # set to None if derivation_formula (nullable) is None
        # and __fields_set__ contains the field
        if self.derivation_formula is None and "derivation_formula" in self.__fields_set__:
            _dict['derivationFormula'] = None

        # set to None if links (nullable) is None
        # and __fields_set__ contains the field
        if self.links is None and "links" in self.__fields_set__:
            _dict['links'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PropertyDefinitionSearchResult:
        """Create an instance of PropertyDefinitionSearchResult from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PropertyDefinitionSearchResult.parse_obj(obj)

        _obj = PropertyDefinitionSearchResult.parse_obj({
            "href": obj.get("href"),
            "key": obj.get("key"),
            "value_type": obj.get("valueType"),
            "display_name": obj.get("displayName"),
            "data_type_id": ResourceId.from_dict(obj.get("dataTypeId")) if obj.get("dataTypeId") is not None else None,
            "type": obj.get("type"),
            "unit_schema": obj.get("unitSchema"),
            "domain": obj.get("domain"),
            "scope": obj.get("scope"),
            "code": obj.get("code"),
            "value_required": obj.get("valueRequired"),
            "life_time": obj.get("lifeTime"),
            "constraint_style": obj.get("constraintStyle"),
            "property_definition_type": obj.get("propertyDefinitionType"),
            "property_description": obj.get("propertyDescription"),
            "derivation_formula": obj.get("derivationFormula"),
            "is_filterable": obj.get("isFilterable"),
            "links": [Link.from_dict(_item) for _item in obj.get("links")] if obj.get("links") is not None else None
        })
        return _obj
