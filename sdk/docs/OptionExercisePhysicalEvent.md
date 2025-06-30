# OptionExercisePhysicalEvent

Event for physical option exercises.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exercise_date** | **datetime** | The exercise date of the option. | [optional] 
**delivery_date** | **datetime** | The delivery date of the option. | [optional] 
**exercise_type** | **str** | The optionality type of the underlying option e.g. American, European.    Supported string (enumeration) values are: [European, Bermudan, American]. | 
**maturity_date** | **datetime** | The maturity date of the option. | [optional] 
**moneyness** | **str** | The moneyness of the option e.g. InTheMoney, OutOfTheMoney.    Supported string (enumeration) values are: [InTheMoney, OutOfTheMoney, AtTheMoney]. | [optional] 
**new_instrument** | [**NewInstrument**](NewInstrument.md) |  | 
**option_exercise_elections** | [**List[OptionExerciseElection]**](OptionExerciseElection.md) | Option exercise election for this OptionExercisePhysicalEvent. | [optional] 
**option_type** | **str** | Type of optionality that is present e.g. call, put.    Supported string (enumeration) values are: [Call, Put]. | 
**start_date** | **datetime** | The trade date of the option. | [optional] 
**strike_currency** | **str** | The strike currency of the equity option. | 
**strike_per_unit** | **float** | The strike of the equity option times the number of shares to exchange if exercised. | 
**underlying_value_per_unit** | **float** | The underlying price times the number of shares to exchange if exercised. | [optional] 
**units_ratio** | [**UnitsRatio**](UnitsRatio.md) |  | 
**instrument_event_type** | **str** | The Type of Event. The available values are: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent, ExpiryEvent, ScripDividendEvent, StockDividendEvent, ReverseStockSplitEvent, CapitalDistributionEvent, SpinOffEvent, MergerEvent, FutureExpiryEvent, SwapCashFlowEvent, SwapPrincipalEvent, CreditPremiumCashFlowEvent, CdsCreditEvent, CdxCreditEvent, MbsCouponEvent, MbsPrincipalEvent, BonusIssueEvent, MbsPrincipalWriteOffEvent, MbsInterestDeferralEvent, MbsInterestShortfallEvent, TenderEvent, CallOnIntermediateSecuritiesEvent, IntermediateSecuritiesDistributionEvent, OptionExercisePhysicalEvent, OptionExerciseCashEvent, ProtectionPayoutCashFlowEvent, TermDepositInterestEvent, TermDepositPrincipalEvent, EarlyRedemptionEvent, FutureMarkToMarketEvent, AdjustGlobalCommitmentEvent, ContractInitialisationEvent, DrawdownEvent, LoanInterestRepaymentEvent, UpdateDepositAmountEvent, LoanPrincipalRepaymentEvent, DepositInterestPaymentEvent, DepositCloseEvent, LoanFacilityContractRolloverEvent, RepurchaseOfferEvent, RepoPartialClosureEvent, RepoCashFlowEvent | 
## Example

```python
from lusid.models.option_exercise_physical_event import OptionExercisePhysicalEvent
from typing import Any, Dict, List, Optional, Union
from pydantic.v1 import Field, StrictFloat, StrictInt, StrictStr, conlist, constr, validator
from datetime import datetime
exercise_date: Optional[datetime] = # Replace with your value
delivery_date: Optional[datetime] = # Replace with your value
exercise_type: StrictStr = "example_exercise_type"
maturity_date: Optional[datetime] = # Replace with your value
moneyness: Optional[StrictStr] = "example_moneyness"
new_instrument: NewInstrument = # Replace with your value
option_exercise_elections: Optional[conlist(OptionExerciseElection)] = # Replace with your value
option_type: StrictStr = "example_option_type"
start_date: Optional[datetime] = # Replace with your value
strike_currency: StrictStr = "example_strike_currency"
strike_per_unit: Union[StrictFloat, StrictInt] = # Replace with your value
underlying_value_per_unit: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
units_ratio: UnitsRatio = # Replace with your value
instrument_event_type: StrictStr = "example_instrument_event_type"
option_exercise_physical_event_instance = OptionExercisePhysicalEvent(exercise_date=exercise_date, delivery_date=delivery_date, exercise_type=exercise_type, maturity_date=maturity_date, moneyness=moneyness, new_instrument=new_instrument, option_exercise_elections=option_exercise_elections, option_type=option_type, start_date=start_date, strike_currency=strike_currency, strike_per_unit=strike_per_unit, underlying_value_per_unit=underlying_value_per_unit, units_ratio=units_ratio, instrument_event_type=instrument_event_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

