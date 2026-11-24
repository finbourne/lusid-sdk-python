# FundCashStatementLocalCurrency

A single row in the local-currency Fund Cash Statement report. Each row is a settled cash  movement with a running balance in local currency, and the base-currency cash flow, realised FX  (split into its trade-date-to-settlement-date and cash pool parts), cost basis, balance at the  recipe's rate on the row's date and the unrealised FX between the two.
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
**cashflow_base** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | [optional] 
**trade_date_to_settlement_date_fx_pnl_base** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | [optional] 
**cash_pool_fx_pnl_base** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | [optional] 
**cost_basis_base** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | [optional] 
**balance_base** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | [optional] 
**unrealised_fx_pnl_base** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | [optional] 
**balance_fx_rate** | **float** | The FX rate BalanceBase was struck at, from the row&#39;s currency to the base currency, or 1 for a balance already in the base currency. Not returned when BalanceBase is not, nor when BalanceLocal is zero and no rate was found. | [optional] 
**balance_base_failure_reason** | **str** | Why BalanceBase, BalanceFxRate and UnrealisedFxPnlBase are not returned on this row: no FX rate was found for the row&#39;s currency at its accounting date within the recipe&#39;s quote interval, the rate found was not positive, or the rates could not be read. Null when the balance was struck, and on a row whose BalanceLocal is zero, which is zero in the base currency without a rate. | [optional] 
**avg_rate** | **float** | Weighted average FX rate (costBasisBase / balanceLocal). Null when balance is zero. | [optional] 
**fx_rate_movement** | **float** | FX rate for this specific movement (CashflowBase / CashFlowLocal). Null when localAmount is zero. | [optional] 
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
cashflow_base: Optional[CurrencyAndAmount] = # Replace with your value
trade_date_to_settlement_date_fx_pnl_base: Optional[CurrencyAndAmount] = # Replace with your value
cash_pool_fx_pnl_base: Optional[CurrencyAndAmount] = # Replace with your value
cost_basis_base: Optional[CurrencyAndAmount] = # Replace with your value
balance_base: Optional[CurrencyAndAmount] = # Replace with your value
unrealised_fx_pnl_base: Optional[CurrencyAndAmount] = # Replace with your value
balance_fx_rate: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
balance_base_failure_reason: Optional[StrictStr] = "example_balance_base_failure_reason"
avg_rate: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
fx_rate_movement: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
links: Optional[List[Link]] = None
fund_cash_statement_local_currency_instance = FundCashStatementLocalCurrency(group_by_id=group_by_id, sequence_number=sequence_number, sub_holding_keys=sub_holding_keys, source_id=source_id, cash_statement_action_type=cash_statement_action_type, entry_type=entry_type, accounting_date=accounting_date, activity_date=activity_date, movement_name=movement_name, portfolio_id=portfolio_id, instruction_type=instruction_type, diary_entry_code=diary_entry_code, origin_diary_entry_code=origin_diary_entry_code, cashflow_local=cashflow_local, balance_local=balance_local, properties=properties, cashflow_base=cashflow_base, trade_date_to_settlement_date_fx_pnl_base=trade_date_to_settlement_date_fx_pnl_base, cash_pool_fx_pnl_base=cash_pool_fx_pnl_base, cost_basis_base=cost_basis_base, balance_base=balance_base, unrealised_fx_pnl_base=unrealised_fx_pnl_base, balance_fx_rate=balance_fx_rate, balance_base_failure_reason=balance_base_failure_reason, avg_rate=avg_rate, fx_rate_movement=fx_rate_movement, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

