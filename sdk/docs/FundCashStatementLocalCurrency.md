# FundCashStatementLocalCurrency

A single row in the local-currency Fund Cash Statement report. Each row is a settled cash  movement with a running balance in local currency only; base-currency columns are out of  scope for this variant and are not returned.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_by_id** | **int** | The groupBy subHoldings and currency. | [optional] 
**sequence_number** | **int** | Sequence number determining the order of the cash flow records. | [optional] 
**sub_holding_keys** | [**Dict[str, PerpetualProperty]**](PerpetualProperty.md) | The sub-holding properties which identify the holding. Each property will be from the &#39;Transaction&#39; domain. These are configured on a transaction portfolio. | [optional] 
**source_id** | **str** | The transaction ID that sourced this cash movement. | [optional] 
**cash_statement_action_type** | **str** | The action type: Default, Reversal, TrueUp, SystemCorrection, Opening, or Closing. | [optional] 
**entry_type** | **str** | What drove the row: SystemGenerated (accounting-engine housekeeping such as a reversal/true-up around a backdated transaction) or UserEntered (a real cash movement booked by a user, e.g. a late trade or amendment). | [optional] 
**accounting_date** | **datetime** | The accounting date of the cash movement. | [optional] 
**activity_date** | **datetime** | The activity date (trade/settlement date) of the cash movement. | [optional] 
**movement_name** | **str** | The movement type (e.g. Receivable_Cash_Trade, Payable_Cash_Trade). | [optional] 
**portfolio_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**instruction_type** | **str** | The settlement instruction type: Automatic, Instructed_Complete, Instructed - Cancel Automatic. | [optional] 
**diary_entry_code** | **str** | The diary entry code of the valuation point this row belongs to. | [optional] 
**origin_diary_entry_code** | **str** | For Reversal/TrueUp rows: the diary entry code of the period the original row belonged to. | [optional] 
**cashflow_local** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | [optional] 
**balance_local** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | [optional] 
**properties** | [**Dict[str, ModelProperty]**](ModelProperty.md) | The requested properties decorated onto the cash statement row. | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.fund_cash_statement_local_currency import FundCashStatementLocalCurrency
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

group_by_id: Optional[StrictInt] = # Replace with your value
group_by_id: Optional[StrictInt] = None
sequence_number: Optional[StrictInt] = # Replace with your value
sequence_number: Optional[StrictInt] = None
sub_holding_keys: Optional[Dict[str, PerpetualProperty]] = # Replace with your value
source_id: Optional[StrictStr] = "example_source_id"
cash_statement_action_type: Optional[StrictStr] = "example_cash_statement_action_type"
entry_type: Optional[StrictStr] = "example_entry_type"
accounting_date: Optional[datetime] = # Replace with your value
activity_date: Optional[datetime] = # Replace with your value
movement_name: Optional[StrictStr] = "example_movement_name"
portfolio_id: Optional[ResourceId] = # Replace with your value
instruction_type: Optional[StrictStr] = "example_instruction_type"
diary_entry_code: Optional[StrictStr] = "example_diary_entry_code"
origin_diary_entry_code: Optional[StrictStr] = "example_origin_diary_entry_code"
cashflow_local: Optional[CurrencyAndAmount] = # Replace with your value
balance_local: Optional[CurrencyAndAmount] = # Replace with your value
properties: Optional[Dict[str, ModelProperty]] = # Replace with your value
links: Optional[List[Link]] = None
fund_cash_statement_local_currency_instance = FundCashStatementLocalCurrency(group_by_id=group_by_id, sequence_number=sequence_number, sub_holding_keys=sub_holding_keys, source_id=source_id, cash_statement_action_type=cash_statement_action_type, entry_type=entry_type, accounting_date=accounting_date, activity_date=activity_date, movement_name=movement_name, portfolio_id=portfolio_id, instruction_type=instruction_type, diary_entry_code=diary_entry_code, origin_diary_entry_code=origin_diary_entry_code, cashflow_local=cashflow_local, balance_local=balance_local, properties=properties, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

