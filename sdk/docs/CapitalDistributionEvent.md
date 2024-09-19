# CapitalDistributionEvent

A capital distribution paid out to shareholders.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**announcement_date** | **datetime** | Date on which the dividend was announced / declared. | [optional] 
**cash_elections** | [**List[CashElection]**](CashElection.md) | Possible elections for this event, each keyed with a unique identifier. | 
**ex_date** | **datetime** | The first business day on which the dividend is not owed to the buying party. | 
**payment_date** | **datetime** | The date the company begins distributing the dividend. | 
**record_date** | **datetime** | Date you have to be the holder of record in order to participate in the tender. | [optional] 
**instrument_event_type** | **str** | The Type of Event. The available values are: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent, ExpiryEvent, ScripDividendEvent, StockDividendEvent, ReverseStockSplitEvent, CapitalDistributionEvent, SpinOffEvent, MergerEvent, FutureExpiryEvent, SwapCashFlowEvent, SwapPrincipalEvent, CreditPremiumCashFlowEvent, CdsCreditEvent, CdxCreditEvent, MbsCouponEvent, MbsPrincipalEvent | 

## Example

```python
from lusid.models.capital_distribution_event import CapitalDistributionEvent

# TODO update the JSON string below
json = "{}"
# create an instance of CapitalDistributionEvent from a JSON string
capital_distribution_event_instance = CapitalDistributionEvent.from_json(json)
# print the JSON string representation of the object
print CapitalDistributionEvent.to_json()

# convert the object into a dict
capital_distribution_event_dict = capital_distribution_event_instance.to_dict()
# create an instance of CapitalDistributionEvent from a dict
capital_distribution_event_form_dict = capital_distribution_event.from_dict(capital_distribution_event_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


