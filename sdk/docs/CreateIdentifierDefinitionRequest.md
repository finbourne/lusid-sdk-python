# CreateIdentifierDefinitionRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** | The type of entity to which the identifier can be attached. Supported values are \&quot;Instrument\&quot;, \&quot;Person\&quot;, \&quot;LegalEntity\&quot;and \&quot;CustomEntity\&quot;. The available values are: NotDefined, Transaction, Portfolio, Holding, ReferenceHolding, TransactionConfiguration, Instrument, CutLabelDefinition, Analytic, PortfolioGroup, Person, AccessMetadata, Order, UnitResult, MarketData, ConfigurationRecipe, Allocation, Calendar, LegalEntity, InvestorRecord, InvestmentAccount, Placement, Execution, Block, Participation, Package, OrderInstruction, NextBestAction, CustomEntity, InstrumentEvent, Account, ChartOfAccounts, CustodianAccount, CheckDefinition, Abor, AborConfiguration, Fund, FundConfiguration, Fee, Reconciliation, PropertyDefinition, Compliance, DiaryEntry, Leg, DerivedValuation, Timeline, ClosedPeriod, AddressKeyDefinition, AmortisationRuleSet, AnalyticsSetInventory, AtomUnitResult, CleardownModule, ComplexMarketData, ComplianceRunSummary, ComplianceRule, ComplianceRunInfo, CorporateActionSource, CounterpartyAgreement, CustomEntityDefinition, DataType, Dialect, EventHandler, GeneralLedgerProfile, PostingModule, Quote, RecipeComposer, ReconciliationRunBreak, ReferenceList, RelationDefinition, ReturnBlockIndex, SRSDocument, SRSIndex, TransactionTemplate, TransactionTemplateScope, TransactionType, TransactionTypeConfig, TranslationScript, TaskDefinition, TaskInstance, Worker, StagingRuleSet, IdentifierDefinition | 
**identifier_scope** | **str** | The scope that the identifier definition exists in. | 
**identifier_type** | **str** | What the identifier represents. Together with \&quot;domain\&quot; and \&quot;identifierScope\&quot; this uniquely identifies the identifier definition. | 
**life_time** | **str** | Describes whether an identifier value is associated with an entity for all effective dates (“Perpetual”) or applies within a specified effective date range (“TimeVariant”). The available values are: Perpetual, TimeVariant | 
**hierarchy_usage** | **str** | Nullable, defaults to \&quot;MasterIdentifier\&quot; if no value provided. \&quot;MasterIdentifier\&quot; (aka unique) An entity can have one value for this identifier definition on a given effective date. A value for this identifier definition can only be associated with one entity (in a given scope) on a given effective date. \&quot;ParentIdentifier\&quot; (aka non-unique) An entity can have one value for this identifier definition on a given effective date. A value for this identifier definition can be associated with many entities (in a given scope) on a given effective date. | [optional] 
**hierarchy_level** | **str** | Optional metadata associated with the identifier definition. | [optional] 
**display_name** | **str** | A display name for the identifier. E.g. Figi. | [optional] 
**description** | **str** | An optional description for the identifier. | [optional] 
**properties** | [**Dict[str, ModelProperty]**](ModelProperty.md) | A set of properties for the identifier definition. | [optional] 
## Example

```python
from lusid.models.create_identifier_definition_request import CreateIdentifierDefinitionRequest
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, constr, validator

domain: StrictStr = "example_domain"
identifier_scope: StrictStr = "example_identifier_scope"
identifier_type: StrictStr = "example_identifier_type"
life_time: StrictStr = "example_life_time"
hierarchy_usage: Optional[StrictStr] = "example_hierarchy_usage"
hierarchy_level: Optional[StrictStr] = "example_hierarchy_level"
display_name: Optional[StrictStr] = "example_display_name"
description: Optional[StrictStr] = "example_description"
properties: Optional[Dict[str, ModelProperty]] = # Replace with your value
create_identifier_definition_request_instance = CreateIdentifierDefinitionRequest(domain=domain, identifier_scope=identifier_scope, identifier_type=identifier_type, life_time=life_time, hierarchy_usage=hierarchy_usage, hierarchy_level=hierarchy_level, display_name=display_name, description=description, properties=properties)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

