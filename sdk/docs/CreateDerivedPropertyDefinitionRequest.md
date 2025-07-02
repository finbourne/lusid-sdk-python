# CreateDerivedPropertyDefinitionRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** | The domain that the property exists in. Not all available values are currently supported, please check the documentation: https://support.lusid.com/knowledgebase/article/KA-01719/. The available values are: NotDefined, Transaction, Portfolio, Holding, ReferenceHolding, TransactionConfiguration, Instrument, CutLabelDefinition, Analytic, PortfolioGroup, Person, AccessMetadata, Order, UnitResult, MarketData, ConfigurationRecipe, Allocation, Calendar, LegalEntity, InvestorRecord, InvestmentAccount, Placement, Execution, Block, Participation, Package, OrderInstruction, NextBestAction, CustomEntity, InstrumentEvent, Account, ChartOfAccounts, CustodianAccount, CheckDefinition, Abor, AborConfiguration, Fund, FundConfiguration, Fee, Reconciliation, PropertyDefinition, Compliance, DiaryEntry, Leg, DerivedValuation, Timeline, ClosedPeriod, AddressKeyDefinition, AmortisationRuleSet, AnalyticsSetInventory, AtomUnitResult, CleardownModule, ComplexMarketData, ComplianceRunSummary, ComplianceRule, ComplianceRunInfo, CorporateActionSource, CounterpartyAgreement, CustomEntityDefinition, DataType, Dialect, EventHandler, GeneralLedgerProfile, PostingModule, Quote, RecipeComposer, ReconciliationRunBreak, ReferenceList, RelationDefinition, ReturnBlockIndex, SRSDocument, SRSIndex, TransactionTemplate, TransactionTemplateScope, TransactionType, TransactionTypeConfig, TranslationScript, TaskDefinition, TaskInstance, Worker, StagingRuleSet, IdentifierDefinition | 
**scope** | **str** | The scope that the property exists in. | 
**code** | **str** | The code of the property. Together with the domain and scope this uniquely identifies the property. | 
**display_name** | **str** | The display name of the property. | 
**data_type_id** | [**ResourceId**](ResourceId.md) |  | 
**property_description** | **str** | Describes the property | [optional] 
**derivation_formula** | **str** | The rule that defines how data is composed for a derived property. | 
**is_filterable** | **bool** | Bool indicating whether the values of this property are fitlerable, this is true for all non-derived property defintions.  For a derived definition this must be set true to enable filtering. | 
## Example

```python
from lusid.models.create_derived_property_definition_request import CreateDerivedPropertyDefinitionRequest
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, StrictBool, StrictStr, constr, validator

domain: StrictStr = "example_domain"
scope: StrictStr = "example_scope"
code: StrictStr = "example_code"
display_name: StrictStr = "example_display_name"
data_type_id: ResourceId = # Replace with your value
property_description: Optional[StrictStr] = "example_property_description"
derivation_formula: StrictStr = "example_derivation_formula"
is_filterable: StrictBool = # Replace with your value
is_filterable:StrictBool = True
create_derived_property_definition_request_instance = CreateDerivedPropertyDefinitionRequest(domain=domain, scope=scope, code=code, display_name=display_name, data_type_id=data_type_id, property_description=property_description, derivation_formula=derivation_formula, is_filterable=is_filterable)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

