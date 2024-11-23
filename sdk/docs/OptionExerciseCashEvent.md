# OptionExerciseCashEvent

Event for cash option exercises.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cash_flow_per_unit** | **float** | The cashflow per unit | [optional] 
**exercise_date** | **datetime** | The exercise date of the option. | [optional] 
**delivery_date** | **datetime** | The delivery date of the option. | [optional] 
**exercise_type** | **str** | The optionality type of the underlying option e.g. American, European.    Supported string (enumeration) values are: [European, Bermudan, American]. | 
**maturity_date** | **datetime** | The maturity date of the option. | 
**moneyness** | **str** | The moneyness of the option e.g. InTheMoney, OutOfTheMoney.    Supported string (enumeration) values are: [InTheMoney, OutOfTheMoney, AtTheMoney]. | [optional] 
**option_exercise_elections** | [**List[OptionExerciseElection]**](OptionExerciseElection.md) | Option exercise election for this OptionExercisePhysicalEvent. | [optional] 
**option_type** | **str** | Type of optionality that is present e.g. call, put.    Supported string (enumeration) values are: [Call, Put]. | 
**start_date** | **datetime** | The start date of the option. | 
**strike_currency** | **str** | The strike currency of the equity option. | 
**strike_per_unit** | **float** | The strike of the equity option times the number of shares to exchange if exercised. | 
**underlying_value_per_unit** | **float** | The underlying price times the number of shares to exchange if exercised. | [optional] 
**instrument_event_type** | **str** | The Type of Event. The available values are: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent, ExpiryEvent, ScripDividendEvent, StockDividendEvent, ReverseStockSplitEvent, CapitalDistributionEvent, SpinOffEvent, MergerEvent, FutureExpiryEvent, SwapCashFlowEvent, SwapPrincipalEvent, CreditPremiumCashFlowEvent, CdsCreditEvent, CdxCreditEvent, MbsCouponEvent, MbsPrincipalEvent, BonusIssueEvent, MbsPrincipalWriteOffEvent, MbsInterestDeferralEvent, MbsInterestShortfallEvent, TenderEvent, CallOnIntermediateSecuritiesEvent, IntermediateSecuritiesDistributionEvent, OptionExercisePhysicalEvent, OptionExerciseCashEvent, ProtectionPayoutCashFlowEvent, TermDepositInterestEvent, TermDepositPrincipalEvent, EarlyRedemptionEvent, FutureMarkToMarketEvent, AdjustGlobalCommitmentEvent, ContractInitialisationEvent, DrawdownEvent | 

## Example

```python
from lusid.models.option_exercise_cash_event import OptionExerciseCashEvent

# TODO update the JSON string below
json = "{}"
# create an instance of OptionExerciseCashEvent from a JSON string
option_exercise_cash_event_instance = OptionExerciseCashEvent.from_json(json)
# print the JSON string representation of the object
print OptionExerciseCashEvent.to_json()

# convert the object into a dict
option_exercise_cash_event_dict = option_exercise_cash_event_instance.to_dict()
# create an instance of OptionExerciseCashEvent from a dict
option_exercise_cash_event_form_dict = option_exercise_cash_event.from_dict(option_exercise_cash_event_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


