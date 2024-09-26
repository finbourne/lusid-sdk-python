# CdxCreditEvent

Definition of a credit event for credit default swap index (CDX) instruments.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**effective_date** | **datetime** | The date of the credit default - i.e. date on which the debt issuer defaulted on its repayment obligation. | 
**auction_date** | **datetime** | The date of the credit event auction - i.e. date on which the defaulted debt is sold via auction, and a recovery rate determined. | [optional] 
**recovery_rate** | **float** | The fraction of the defaulted debt that can be recovered. | [optional] 
**constituent_weight** | **float** | The relative weight of the CDX constituent. | 
**constituent_reference** | **str** | Reference value used to identify the CDX constituent. | [optional] 
**instrument_event_type** | **str** | The Type of Event. The available values are: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent, ExpiryEvent, ScripDividendEvent, StockDividendEvent, ReverseStockSplitEvent, CapitalDistributionEvent, SpinOffEvent, MergerEvent, FutureExpiryEvent, SwapCashFlowEvent, SwapPrincipalEvent, CreditPremiumCashFlowEvent, CdsCreditEvent, CdxCreditEvent, MbsCouponEvent, MbsPrincipalEvent, BonusIssueEvent | 

## Example

```python
from lusid.models.cdx_credit_event import CdxCreditEvent

# TODO update the JSON string below
json = "{}"
# create an instance of CdxCreditEvent from a JSON string
cdx_credit_event_instance = CdxCreditEvent.from_json(json)
# print the JSON string representation of the object
print CdxCreditEvent.to_json()

# convert the object into a dict
cdx_credit_event_dict = cdx_credit_event_instance.to_dict()
# create an instance of CdxCreditEvent from a dict
cdx_credit_event_form_dict = cdx_credit_event.from_dict(cdx_credit_event_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


