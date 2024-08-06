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
**domain** | **str** | The domain that the property exists in. The available values are: NotDefined, Transaction, Portfolio, Holding, ReferenceHolding, TransactionConfiguration, Instrument, CutLabelDefinition, Analytic, PortfolioGroup, Person, AccessMetadata, Order, UnitResult, MarketData, ConfigurationRecipe, Allocation, Calendar, LegalEntity, Placement, Execution, Block, Participation, Package, OrderInstruction, NextBestAction, CustomEntity, InstrumentEvent, Account, ChartOfAccounts, CustodianAccount, Abor, AborConfiguration, Fund, FundConfiguration, Fee, Reconciliation, PropertyDefinition, Compliance, DiaryEntry, Leg, DerivedValuation, AddressKeyDefinition, AmortisationRuleSet, AnalyticsSetInventory, AtomUnitResult, CleardownModule, ComplexMarketData, ComplianceRunSummary, ComplianceRule, ComplianceRunInfo, CorporateActionSource, CounterpartyAgreement, CustomEntityDefinition, DataType, Dialect, EventHandler, GeneralLedgerProfile, PostingModule, Quote, RecipeComposer, ReconciliationRunBreak, ReferenceList, RelationDefinition, ReturnBlockIndex, SRSDocument, SRSIndex, TransactionTemplate, TransactionTemplateScope, TransactionType, TransactionTypeConfig, TranslationScript, TaskDefinition, TaskInstance, Worker, StagingRuleSet | [optional] 
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
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.property_definition import PropertyDefinition

# TODO update the JSON string below
json = "{}"
# create an instance of PropertyDefinition from a JSON string
property_definition_instance = PropertyDefinition.from_json(json)
# print the JSON string representation of the object
print PropertyDefinition.to_json()

# convert the object into a dict
property_definition_dict = property_definition_instance.to_dict()
# create an instance of PropertyDefinition from a dict
property_definition_form_dict = property_definition.from_dict(property_definition_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


