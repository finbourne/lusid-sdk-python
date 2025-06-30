# PortfolioCashFlow

The details for the cashflow for a given portfolio.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_by_id** | **int** | The groupBy subHoldings and currency. | 
**sequence_number** | **int** | Sequence number determining the order of the cash flow records. | 
**effective_date** | **datetime** | Indicates the date when the cash-flow settles. | [optional] 
**sub_holding_keys** | [**Dict[str, PerpetualProperty]**](PerpetualProperty.md) | The sub-holding properties which identify the holding. Each property will be from the &#39;Transaction&#39; domain. These are configured on a transaction portfolio. | [optional] 
**type** | **str** | Indicates the record type (Closed, Open, Activity). | 
**movement_name** | **str** | Indicates the specific movement of the transaction that generated this cash flow. | 
**cashflow** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | 
**balance** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | 
**fx_rate** | **float** | Exchange rate between the currency of this cash flow and the reporting currency. | 
**cashflow_reporting_currency** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | 
**balance_reporting_currency** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | 
**translation_gain_loss** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | 
**cost_basis_reporting_currency** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | 
**transaction** | [**Transaction**](Transaction.md) |  | [optional] 
**unrealised_gain_loss_reporting_currency** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.portfolio_cash_flow import PortfolioCashFlow
from typing import Any, Dict, List, Optional, Union
from pydantic.v1 import BaseModel, Field, StrictFloat, StrictInt, conlist, constr
from datetime import datetime
group_by_id: StrictInt = # Replace with your value
group_by_id: StrictInt = 42
sequence_number: StrictInt = # Replace with your value
sequence_number: StrictInt = 42
effective_date: Optional[datetime] = # Replace with your value
sub_holding_keys: Optional[Dict[str, PerpetualProperty]] = # Replace with your value
type: StrictStr = "example_type"
movement_name: StrictStr = "example_movement_name"
cashflow: CurrencyAndAmount = # Replace with your value
balance: CurrencyAndAmount = # Replace with your value
fx_rate: Union[StrictFloat, StrictInt] = # Replace with your value
cashflow_reporting_currency: CurrencyAndAmount = # Replace with your value
balance_reporting_currency: CurrencyAndAmount = # Replace with your value
translation_gain_loss: CurrencyAndAmount = # Replace with your value
cost_basis_reporting_currency: CurrencyAndAmount = # Replace with your value
transaction: Optional[Transaction] = None
unrealised_gain_loss_reporting_currency: CurrencyAndAmount = # Replace with your value
links: Optional[conlist(Link)] = None
portfolio_cash_flow_instance = PortfolioCashFlow(group_by_id=group_by_id, sequence_number=sequence_number, effective_date=effective_date, sub_holding_keys=sub_holding_keys, type=type, movement_name=movement_name, cashflow=cashflow, balance=balance, fx_rate=fx_rate, cashflow_reporting_currency=cashflow_reporting_currency, balance_reporting_currency=balance_reporting_currency, translation_gain_loss=translation_gain_loss, cost_basis_reporting_currency=cost_basis_reporting_currency, transaction=transaction, unrealised_gain_loss_reporting_currency=unrealised_gain_loss_reporting_currency, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

