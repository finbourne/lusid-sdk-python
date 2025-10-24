# CreatePropertyDefinitionRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** | The domain that the property exists in. The available values are: NotDefined, Transaction, Portfolio, Holding, ReferenceHolding, TransactionConfiguration, Instrument, CutLabelDefinition, Analytic, PortfolioGroup, Person, AccessMetadata, Order, UnitResult, MarketData, ConfigurationRecipe, Allocation, Calendar, LegalEntity, InvestorRecord, InvestmentAccount, Placement, Execution, Block, Participation, Package, OrderInstruction, NextBestAction, CustomEntity, InstrumentEvent, Account, ChartOfAccounts, CustodianAccount, CheckDefinition, Abor, AborConfiguration, Fund, FundConfiguration, Fee, Reconciliation, PropertyDefinition, Compliance, DiaryEntry, Leg, DerivedValuation, Timeline, ClosedPeriod, AddressKeyDefinition, AmortisationRuleSet, AnalyticsSetInventory, AtomUnitResult, CleardownModule, ComplexMarketData, ComplianceRunSummary, ComplianceRule, ComplianceRunInfo, CorporateActionSource, CounterpartyAgreement, CustomEntityDefinition, DataType, Dialect, EventHandler, GeneralLedgerProfile, PostingModule, Quote, RecipeComposer, ReconciliationRunBreak, ReferenceList, RelationDefinition, ReturnBlockIndex, SRSDocument, SRSIndex, TransactionTemplate, TransactionTemplateScope, TransactionType, TransactionTypeConfig, TranslationScript, TaskDefinition, TaskInstance, Worker, StagingRuleSet, IdentifierDefinition, SettlementInstruction | 
**scope** | **str** | The scope that the property exists in. | 
**code** | **str** | The code of the property. Together with the domain and scope this uniquely identifies the property. | 
**value_required** | **bool** | This field is not implemented and should be disregarded. | [optional] 
**display_name** | **str** | The display name of the property. | 
**data_type_id** | [**ResourceId**](ResourceId.md) |  | 
**life_time** | **str** | Describes how the property&#39;s values can change over time. The available values are: Perpetual, TimeVariant | [optional] 
**constraint_style** | **str** | Describes the uniqueness and cardinality of the property for entity objects under the property domain specified in Key. Defaults to \&quot;Property\&quot; if not specified. Valid values for this field are: Property, Collection or Identifier. | [optional] 
**property_description** | **str** | Describes the property | [optional] 
**collection_type** | **str** | Describes whether a collection property should behave as a set or as an array. | [optional] 
**custom_entity_types** | **List[str]** | The custom entity types that properties relating to this property definition can be applied to. | [optional] 
## Example

```python
from lusid.models.create_property_definition_request import CreatePropertyDefinitionRequest
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictBool, StrictStr, conlist, constr, validator

domain: StrictStr = "example_domain"
scope: StrictStr = "example_scope"
code: StrictStr = "example_code"
value_required: Optional[StrictBool] = # Replace with your value
value_required:Optional[StrictBool] = None
display_name: StrictStr = "example_display_name"
data_type_id: ResourceId = # Replace with your value
life_time: Optional[StrictStr] = "example_life_time"
constraint_style: Optional[StrictStr] = "example_constraint_style"
property_description: Optional[StrictStr] = "example_property_description"
collection_type: Optional[StrictStr] = "example_collection_type"
custom_entity_types: Optional[conlist(StrictStr)] = # Replace with your value
create_property_definition_request_instance = CreatePropertyDefinitionRequest(domain=domain, scope=scope, code=code, value_required=value_required, display_name=display_name, data_type_id=data_type_id, life_time=life_time, constraint_style=constraint_style, property_description=property_description, collection_type=collection_type, custom_entity_types=custom_entity_types)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

