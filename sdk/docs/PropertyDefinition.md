# PropertyDefinition

A list of property definitions.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**key** | **str** | The property key which uniquely identifies the property. The format for the property key is {domain}/{scope}/{code}, e.g. &#39;Portfolio/Manager/Id&#39;. | [optional] 
**value_type** | **str** | The type of values that can be associated with this property. This is defined by the property&#39;s data type. The available values are: String, Int, Decimal, DateTime, Boolean, Map, List, PropertyArray, Percentage, Code, Id, Uri, CurrencyAndAmount, TradePrice, Currency, MetricValue, ResourceId, ResultValue, CutLocalTime, DateOrCutLabel, UnindexedText | [optional] 
**display_name** | **str** | The display name of the property. | [optional] 
**data_type_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**type** | **str** | The type of the property. The available values are: Label, Metric, Information | [optional] 
**unit_schema** | **str** | The units that can be associated with the property&#39;s values. This is defined by the property&#39;s data type. The available values are: NoUnits, Basic, Iso4217Currency | [optional] 
**domain** | **str** | The domain that the property exists in. The available values are: NotDefined, Transaction, Portfolio, Holding, ReferenceHolding, TransactionConfiguration, Instrument, CutLabelDefinition, Analytic, PortfolioGroup, Person, AccessMetadata, Order, UnitResult, MarketData, ConfigurationRecipe, Allocation, Calendar, LegalEntity, InvestorRecord, Placement, Execution, Block, Participation, Package, OrderInstruction, NextBestAction, CustomEntity, InstrumentEvent, Account, ChartOfAccounts, CustodianAccount, Abor, AborConfiguration, Fund, FundConfiguration, Fee, Reconciliation, PropertyDefinition, Compliance, DiaryEntry, Leg, DerivedValuation, Timeline, ClosedPeriod, AddressKeyDefinition, AmortisationRuleSet, AnalyticsSetInventory, AtomUnitResult, CleardownModule, ComplexMarketData, ComplianceRunSummary, ComplianceRule, ComplianceRunInfo, CorporateActionSource, CounterpartyAgreement, CustomEntityDefinition, DataType, Dialect, EventHandler, GeneralLedgerProfile, PostingModule, Quote, RecipeComposer, ReconciliationRunBreak, ReferenceList, RelationDefinition, ReturnBlockIndex, SRSDocument, SRSIndex, TransactionTemplate, TransactionTemplateScope, TransactionType, TransactionTypeConfig, TranslationScript, TaskDefinition, TaskInstance, Worker, StagingRuleSet, IdentifierDefinition | [optional] 
**scope** | **str** | The scope that the property exists in. | [optional] [readonly] 
**code** | **str** | The code of the property. Together with the domain and scope this uniquely identifies the property. | [optional] [readonly] 
**value_required** | **bool** | This field is not implemented and should be disregarded. | [optional] 
**life_time** | **str** | Describes how the property&#39;s values can change over time. The available values are: Perpetual, TimeVariant | [optional] 
**constraint_style** | **str** | Describes the uniqueness and cardinality of the property for entity objects under the property domain specified in Key. | [optional] 
**property_definition_type** | **str** | The definition type (DerivedDefinition or Definition). The available values are: ValueProperty, DerivedDefinition | [optional] 
**property_description** | **str** | A brief description of what a property of this property definition contains. | [optional] 
**derivation_formula** | **str** | The rule that defines how data is composed for a derived property. | [optional] 
**collection_type** | **str** | Describes whether a collection property should behave as a set or as an array. | [optional] 
**properties** | [**Dict[str, ModelProperty]**](ModelProperty.md) | Set of unique property definition properties and associated values to store with the property definition. Each property must be from the &#39;PropertyDefinition&#39; domain. | [optional] 
**version** | [**Version**](Version.md) |  | [optional] 
**staged_modifications** | [**StagedModificationsInfo**](StagedModificationsInfo.md) |  | [optional] 
**is_filterable** | **bool** | Bool indicating whether the values of this property are fitlerable, this is true for all non-derived property defintions.  For a derived definition this must be set true to enable filtering. | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.property_definition import PropertyDefinition
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictBool, StrictStr, conlist, validator

href: Optional[StrictStr] = "example_href"
key: Optional[StrictStr] = "example_key"
value_type: Optional[StrictStr] = "example_value_type"
display_name: Optional[StrictStr] = "example_display_name"
data_type_id: Optional[ResourceId] = # Replace with your value
type: Optional[StrictStr] = "example_type"
unit_schema: Optional[StrictStr] = "example_unit_schema"
domain: Optional[StrictStr] = "example_domain"
scope: Optional[StrictStr] = "example_scope"
code: Optional[StrictStr] = "example_code"
value_required: Optional[StrictBool] = # Replace with your value
value_required:Optional[StrictBool] = None
life_time: Optional[StrictStr] = "example_life_time"
constraint_style: Optional[StrictStr] = "example_constraint_style"
property_definition_type: Optional[StrictStr] = "example_property_definition_type"
property_description: Optional[StrictStr] = "example_property_description"
derivation_formula: Optional[StrictStr] = "example_derivation_formula"
collection_type: Optional[StrictStr] = "example_collection_type"
properties: Optional[Dict[str, ModelProperty]] = # Replace with your value
version: Optional[Version] = None
staged_modifications: Optional[StagedModificationsInfo] = # Replace with your value
is_filterable: Optional[StrictBool] = # Replace with your value
is_filterable:Optional[StrictBool] = None
links: Optional[conlist(Link)] = None
property_definition_instance = PropertyDefinition(href=href, key=key, value_type=value_type, display_name=display_name, data_type_id=data_type_id, type=type, unit_schema=unit_schema, domain=domain, scope=scope, code=code, value_required=value_required, life_time=life_time, constraint_style=constraint_style, property_definition_type=property_definition_type, property_description=property_description, derivation_formula=derivation_formula, collection_type=collection_type, properties=properties, version=version, staged_modifications=staged_modifications, is_filterable=is_filterable, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

