# CreatePropertyDefinitionRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** | The domain that the property exists in. The available values are: NotDefined, Transaction, Portfolio, Holding, ReferenceHolding, TransactionConfiguration, Instrument, CutLabelDefinition, Analytic, PortfolioGroup, Person, AccessMetadata, Order, UnitResult, MarketData, ConfigurationRecipe, Allocation, Calendar, LegalEntity, Placement, Execution, Block, Participation, Package, OrderInstruction, NextBestAction, CustomEntity, InstrumentEvent, Account, ChartOfAccounts, CustodianAccount, Abor, AborConfiguration, Fund, FundConfiguration, Fee, Reconciliation, PropertyDefinition, Compliance, DiaryEntry, Leg, DerivedValuation, AddressKeyDefinition, AmortisationRuleSet, AnalyticsSetInventory, AtomUnitResult, CleardownModule, ComplexMarketData, ComplianceRunSummary, ComplianceRule, ComplianceRunInfo, CorporateActionSource, CounterpartyAgreement, CustomEntityDefinition, DataType, Dialect, EventHandler, GeneralLedgerProfile, PostingModule, Quote, RecipeComposer, ReconciliationRunBreak, ReferenceList, RelationDefinition, ReturnBlockIndex, SRSDocument, SRSIndex, TransactionTemplate, TransactionTemplateScope, TransactionType, TransactionTypeConfig, TranslationScript, TaskDefinition, TaskInstance, Worker, StagingRuleSet | 
**scope** | **str** | The scope that the property exists in. | 
**code** | **str** | The code of the property. Together with the domain and scope this uniquely identifies the property. | 
**value_required** | **bool** | This field is not implemented and should be disregarded. | [optional] 
**display_name** | **str** | The display name of the property. | 
**data_type_id** | [**ResourceId**](ResourceId.md) |  | 
**life_time** | **str** | Describes how the property&#39;s values can change over time. The available values are: Perpetual, TimeVariant | [optional] 
**constraint_style** | **str** | Describes the uniqueness and cardinality of the property for entity objects under the property domain specified in Key. Defaults to \&quot;Property\&quot; if not specified. Valid values for this field are: Property, Collection or Identifier. | [optional] 
**property_description** | **str** | Describes the property | [optional] 
**collection_type** | **str** | Describes whether a collection property should behave as a set or as an array. | [optional] 

## Example

```python
from lusid.models.create_property_definition_request import CreatePropertyDefinitionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePropertyDefinitionRequest from a JSON string
create_property_definition_request_instance = CreatePropertyDefinitionRequest.from_json(json)
# print the JSON string representation of the object
print CreatePropertyDefinitionRequest.to_json()

# convert the object into a dict
create_property_definition_request_dict = create_property_definition_request_instance.to_dict()
# create an instance of CreatePropertyDefinitionRequest from a dict
create_property_definition_request_form_dict = create_property_definition_request.from_dict(create_property_definition_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


