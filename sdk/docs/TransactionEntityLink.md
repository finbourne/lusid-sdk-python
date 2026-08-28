# TransactionEntityLink

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_type** | **str** | Available values: Transaction, Portfolio, Holding, ReferenceHolding, TransactionConfiguration, Instrument, PortfolioGroup, Person, Order, Allocation, Calendar, LegalEntity, InvestorRecord, InvestmentAccount, Placement, Execution, Block, Participation, Package, OrderInstruction, CustomEntity, InstrumentEvent, Account, ChartOfAccounts, CustodianAccount, CheckDefinition, Abor, AborConfiguration, Fund, FundConfiguration, FundStructure, Fee, Reconciliation, PropertyDefinition, Compliance, DiaryEntry, Leg, DerivedValuation, Timeline, ClosedPeriod, TaskDefinition, Workflow, IdentifierDefinition, SettlementInstruction, TransactionFeeType, PaymentInstruction, Transfer. | 
**entity_id_name** | **str** |  | 
**entity_id_value** | **str** |  | 
**restrict_editing** | **bool** |  | 
## Example

```python
from lusid.models.transaction_entity_link import TransactionEntityLink
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

entity_type: StrictStr = "example_entity_type"
entity_id_name: StrictStr = "example_entity_id_name"
entity_id_value: StrictStr = "example_entity_id_value"
restrict_editing: StrictBool = # Replace with your value
restrict_editing:StrictBool = True
transaction_entity_link_instance = TransactionEntityLink(entity_type=entity_type, entity_id_name=entity_id_name, entity_id_value=entity_id_value, restrict_editing=restrict_editing)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

