# StockSplitEvent

A split in the company's shares. Shareholders are given additional company shares based on the terms of the stock split.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_date** | **datetime** | Date on which the stock split takes effect. | 
**ex_date** | **datetime** | The first date on which the shares will trade at the post-split price. | 
**units_ratio** | [**UnitsRatio**](UnitsRatio.md) |  | 
**record_date** | **datetime** | Date you have to be the holder of record in order to receive the additional shares. | [optional] 
**announcement_date** | **datetime** | Date the stock split was announced. | [optional] 
**fractional_units_cash_price** | **float** | The cash price per unit paid in lieu when fractional units can not be distributed. | [optional] 
**fractional_units_cash_currency** | **str** | The currency of the cash paid in lieu of fractional units. | [optional] 
**instrument_event_type** | **str** | The Type of Event. The available values are: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent, ExpiryEvent, ScripDividendEvent, StockDividendEvent, ReverseStockSplitEvent, CapitalDistributionEvent, SpinOffEvent, MergerEvent, FutureExpiryEvent, SwapCashFlowEvent, SwapPrincipalEvent, CreditPremiumCashFlowEvent, CdsCreditEvent, CdxCreditEvent | 

## Example

```python
from lusid.models.stock_split_event import StockSplitEvent

# TODO update the JSON string below
json = "{}"
# create an instance of StockSplitEvent from a JSON string
stock_split_event_instance = StockSplitEvent.from_json(json)
# print the JSON string representation of the object
print StockSplitEvent.to_json()

# convert the object into a dict
stock_split_event_dict = stock_split_event_instance.to_dict()
# create an instance of StockSplitEvent from a dict
stock_split_event_form_dict = stock_split_event.from_dict(stock_split_event_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


