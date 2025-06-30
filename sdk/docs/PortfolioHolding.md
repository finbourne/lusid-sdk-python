# PortfolioHolding

A list of holdings.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instrument_scope** | **str** | The scope in which the holding&#39;s instrument is in. | [optional] 
**instrument_uid** | **str** | The unique Lusid Instrument Id (LUID) of the instrument that the holding is in. | 
**sub_holding_keys** | [**Dict[str, PerpetualProperty]**](PerpetualProperty.md) | The sub-holding properties which identify the holding. Each property will be from the &#39;Transaction&#39; domain. These are configured on a transaction portfolio. | [optional] 
**properties** | [**Dict[str, ModelProperty]**](ModelProperty.md) | The properties which have been requested to be decorated onto the holding. These will be from the &#39;Instrument&#39; or &#39;Holding&#39; domain. | [optional] 
**holding_type** | **str** | The code for the type of the holding e.g. P, B, C, R, F etc. | 
**units** | **float** | The total number of units of the holding. | 
**settled_units** | **float** | The total number of settled units of the holding. | 
**cost** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | 
**cost_portfolio_ccy** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | 
**transaction** | [**Transaction**](Transaction.md) |  | [optional] 
**currency** | **str** | The holding currency. | [optional] 
**holding_type_name** | **str** | The decoded type of the holding e.g. Position, Balance, CashCommitment, Receivable, ForwardFX etc. | [optional] 
**holding_id** | **int** | A single identifier for the holding within the portfolio. The holdingId is constructed from the LusidInstrumentId, sub-holding keys and currrency and is unique within the portfolio. | [optional] 
**notional_cost** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | [optional] 
**amortised_cost** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | [optional] 
**amortised_cost_portfolio_ccy** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | [optional] 
**variation_margin** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | [optional] 
**variation_margin_portfolio_ccy** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | [optional] 
**settlement_schedule** | [**List[SettlementSchedule]**](SettlementSchedule.md) | Where no. of days ahead has been specified, future dated settlements will be captured here. | [optional] 
**current_face** | **float** | Current face value of the holding. | [optional] 
## Example

```python
from lusid.models.portfolio_holding import PortfolioHolding
from typing import Any, Dict, List, Optional, Union
from pydantic.v1 import BaseModel, Field, StrictFloat, StrictInt, StrictStr, conlist, constr

instrument_scope: Optional[StrictStr] = "example_instrument_scope"
instrument_uid: StrictStr = "example_instrument_uid"
sub_holding_keys: Optional[Dict[str, PerpetualProperty]] = # Replace with your value
properties: Optional[Dict[str, ModelProperty]] = # Replace with your value
holding_type: StrictStr = "example_holding_type"
units: Union[StrictFloat, StrictInt] = # Replace with your value
settled_units: Union[StrictFloat, StrictInt] = # Replace with your value
cost: CurrencyAndAmount = # Replace with your value
cost_portfolio_ccy: CurrencyAndAmount = # Replace with your value
transaction: Optional[Transaction] = None
currency: Optional[StrictStr] = "example_currency"
holding_type_name: Optional[StrictStr] = "example_holding_type_name"
holding_id: Optional[StrictInt] = # Replace with your value
notional_cost: Optional[CurrencyAndAmount] = # Replace with your value
amortised_cost: Optional[CurrencyAndAmount] = # Replace with your value
amortised_cost_portfolio_ccy: Optional[CurrencyAndAmount] = # Replace with your value
variation_margin: Optional[CurrencyAndAmount] = # Replace with your value
variation_margin_portfolio_ccy: Optional[CurrencyAndAmount] = # Replace with your value
settlement_schedule: Optional[conlist(SettlementSchedule)] = # Replace with your value
current_face: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
portfolio_holding_instance = PortfolioHolding(instrument_scope=instrument_scope, instrument_uid=instrument_uid, sub_holding_keys=sub_holding_keys, properties=properties, holding_type=holding_type, units=units, settled_units=settled_units, cost=cost, cost_portfolio_ccy=cost_portfolio_ccy, transaction=transaction, currency=currency, holding_type_name=holding_type_name, holding_id=holding_id, notional_cost=notional_cost, amortised_cost=amortised_cost, amortised_cost_portfolio_ccy=amortised_cost_portfolio_ccy, variation_margin=variation_margin, variation_margin_portfolio_ccy=variation_margin_portfolio_ccy, settlement_schedule=settlement_schedule, current_face=current_face)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

