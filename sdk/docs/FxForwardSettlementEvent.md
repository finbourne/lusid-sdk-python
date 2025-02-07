# FxForwardSettlementEvent

Settlement for FX Forward, including NDF and deliverable.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**maturity_date** | **datetime** | Maturity date of the forward | 
**dom_amount_per_unit** | **float** | Amount per unit in the DomCcy (domestic currency) | 
**dom_ccy** | **str** | The domestic currency of the forward | 
**fgn_amount_per_unit** | **float** | Amount per unit in the FgnCcy (foreign currency) | 
**fgn_ccy** | **str** | The foreign currency of the forward. | 
**is_ndf** | **bool** | Is this settlement corresponding to a deliverable forward, or an NDF | 
**fixing_date** | **datetime** | Optional.  Required if the event is an NDF (i.e. if IsNdf &#x3D; true).  Date of the FxRate fixings. | [optional] 
**settlement_ccy** | **str** | Optional.  Required if the event is an NDF (i.e. if IsNdf &#x3D; true).  May be set to either DomCcy or FgnCcy, or a third currency. | [optional] 
**cash_flow_per_unit** | **float** | Optional.  Required if the event is an NDF (i.e. if IsNdf &#x3D; true).  CashFlow per unit.  Paid in the SettlementCcy. | [optional] 
**domestic_to_foreign_rate** | **float** | Domestic currency to foreign currency FX rate.  Not required, only used to override quotes. | [optional] 
**domestic_to_settlement_rate** | **float** | Domestic currency to settlement currency FX rate  Not required, only used to override quotes. | [optional] 
**foreign_to_settlement_rate** | **float** | Foreign currency to settlement currency FX rate  Not required, only used to override quotes. | [optional] [readonly] 
**instrument_event_type** | **str** | The Type of Event. The available values are: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent, ExpiryEvent, ScripDividendEvent, StockDividendEvent, ReverseStockSplitEvent, CapitalDistributionEvent, SpinOffEvent, MergerEvent, FutureExpiryEvent, SwapCashFlowEvent, SwapPrincipalEvent, CreditPremiumCashFlowEvent, CdsCreditEvent, CdxCreditEvent, MbsCouponEvent, MbsPrincipalEvent, BonusIssueEvent, MbsPrincipalWriteOffEvent, MbsInterestDeferralEvent, MbsInterestShortfallEvent, TenderEvent, CallOnIntermediateSecuritiesEvent, IntermediateSecuritiesDistributionEvent, OptionExercisePhysicalEvent, OptionExerciseCashEvent, ProtectionPayoutCashFlowEvent, TermDepositInterestEvent, TermDepositPrincipalEvent, EarlyRedemptionEvent, FutureMarkToMarketEvent, AdjustGlobalCommitmentEvent, ContractInitialisationEvent, DrawdownEvent, LoanInterestRepaymentEvent, UpdateDepositAmountEvent, LoanPrincipalRepaymentEvent | 

## Example

```python
from lusid.models.fx_forward_settlement_event import FxForwardSettlementEvent

# TODO update the JSON string below
json = "{}"
# create an instance of FxForwardSettlementEvent from a JSON string
fx_forward_settlement_event_instance = FxForwardSettlementEvent.from_json(json)
# print the JSON string representation of the object
print FxForwardSettlementEvent.to_json()

# convert the object into a dict
fx_forward_settlement_event_dict = fx_forward_settlement_event_instance.to_dict()
# create an instance of FxForwardSettlementEvent from a dict
fx_forward_settlement_event_form_dict = fx_forward_settlement_event.from_dict(fx_forward_settlement_event_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


