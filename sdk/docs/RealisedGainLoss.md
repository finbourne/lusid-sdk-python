# RealisedGainLoss

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instrument_scope** | **str** | The scope in which the instrument lies. | [optional] 
**instrument_uid** | **str** | The unique Lusid Instrument Id (LUID) of the instrument that this gain or loss is associated with. | 
**units** | **float** | The number of units of the associated instrument against which the gain or loss has been realised. | 
**purchase_trade_date** | **datetime** | The effective datetime at which the units associated with this gain or loss were originally purchased. | [optional] [readonly] 
**purchase_settlement_date** | **datetime** | The effective datetime at which the units associated with this gain or loss were originally settled. | [optional] [readonly] 
**purchase_price** | **float** | The purchase price of each unit associated with this gain or loss. | [optional] 
**cost_trade_ccy** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | 
**cost_portfolio_ccy** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | 
**realised_trade_ccy** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | 
**realised_total** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | 
**realised_market** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | [optional] 
**realised_currency** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | [optional] 
**tax_lot_id** | **str** | The identifier of the tax lot with which this gain or loss is associated. | [optional] 
**realised_amortisation** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | [optional] 
## Example

```python
from lusid.models.realised_gain_loss import RealisedGainLoss
from typing import Any, Dict, Optional, Union
from pydantic.v1 import BaseModel, Field, StrictFloat, StrictInt, StrictStr, constr
from datetime import datetime
instrument_scope: Optional[StrictStr] = "example_instrument_scope"
instrument_uid: StrictStr = "example_instrument_uid"
units: Union[StrictFloat, StrictInt] = # Replace with your value
purchase_trade_date: Optional[datetime] = # Replace with your value
purchase_settlement_date: Optional[datetime] = # Replace with your value
purchase_price: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
cost_trade_ccy: CurrencyAndAmount = # Replace with your value
cost_portfolio_ccy: CurrencyAndAmount = # Replace with your value
realised_trade_ccy: CurrencyAndAmount = # Replace with your value
realised_total: CurrencyAndAmount = # Replace with your value
realised_market: Optional[CurrencyAndAmount] = # Replace with your value
realised_currency: Optional[CurrencyAndAmount] = # Replace with your value
tax_lot_id: Optional[StrictStr] = "example_tax_lot_id"
realised_amortisation: Optional[CurrencyAndAmount] = # Replace with your value
realised_gain_loss_instance = RealisedGainLoss(instrument_scope=instrument_scope, instrument_uid=instrument_uid, units=units, purchase_trade_date=purchase_trade_date, purchase_settlement_date=purchase_settlement_date, purchase_price=purchase_price, cost_trade_ccy=cost_trade_ccy, cost_portfolio_ccy=cost_portfolio_ccy, realised_trade_ccy=realised_trade_ccy, realised_total=realised_total, realised_market=realised_market, realised_currency=realised_currency, tax_lot_id=tax_lot_id, realised_amortisation=realised_amortisation)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

