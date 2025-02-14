# BonusIssueEvent

Representation of a Bonus Issue corporate action.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**announcement_date** | **datetime** | The date the Bonus Issue is announced. | [optional] 
**ex_date** | **datetime** | The ex-date of the Bonus Issue. | 
**record_date** | **datetime** | The record date of the Bonus Issue. | [optional] 
**payment_date** | **datetime** | The date the Bonus Issue is executed. | 
**fractional_units_cash_price** | **float** | Optional. Used in calculating cash-in-lieu of fractional shares. | [optional] 
**fractional_units_cash_currency** | **str** | Optional. Used in calculating cash-in-lieu of fractional shares. | [optional] 
**security_offer_elections** | [**List[SecurityOfferElection]**](SecurityOfferElection.md) | Possible SecurityElections for this Bonus Issue event, if any. | [optional] 
**cash_offer_elections** | [**List[CashOfferElection]**](CashOfferElection.md) | Possible CashOfferElections for this Bonus Issue event, if any. | [optional] 
**lapse_elections** | [**List[LapseElection]**](LapseElection.md) | Possible LapseElections for this Bonus Issue event, if any. | [optional] 
**instrument_event_type** | **str** | The Type of Event. The available values are: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent, ExpiryEvent, ScripDividendEvent, StockDividendEvent, ReverseStockSplitEvent, CapitalDistributionEvent, SpinOffEvent, MergerEvent, FutureExpiryEvent, SwapCashFlowEvent, SwapPrincipalEvent, CreditPremiumCashFlowEvent, CdsCreditEvent, CdxCreditEvent, MbsCouponEvent, MbsPrincipalEvent, BonusIssueEvent, MbsPrincipalWriteOffEvent, MbsInterestDeferralEvent, MbsInterestShortfallEvent, TenderEvent, CallOnIntermediateSecuritiesEvent, IntermediateSecuritiesDistributionEvent, OptionExercisePhysicalEvent, OptionExerciseCashEvent, ProtectionPayoutCashFlowEvent, TermDepositInterestEvent, TermDepositPrincipalEvent, EarlyRedemptionEvent, FutureMarkToMarketEvent, AdjustGlobalCommitmentEvent, ContractInitialisationEvent, DrawdownEvent, LoanInterestRepaymentEvent, UpdateDepositAmountEvent, LoanPrincipalRepaymentEvent, DepositInterestPaymentEvent, DepositCloseEvent | 

## Example

```python
from lusid.models.bonus_issue_event import BonusIssueEvent

# TODO update the JSON string below
json = "{}"
# create an instance of BonusIssueEvent from a JSON string
bonus_issue_event_instance = BonusIssueEvent.from_json(json)
# print the JSON string representation of the object
print BonusIssueEvent.to_json()

# convert the object into a dict
bonus_issue_event_dict = bonus_issue_event_instance.to_dict()
# create an instance of BonusIssueEvent from a dict
bonus_issue_event_form_dict = bonus_issue_event.from_dict(bonus_issue_event_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


