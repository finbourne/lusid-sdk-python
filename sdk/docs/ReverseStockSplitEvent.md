# ReverseStockSplitEvent

A reverse split in the company's shares. Shareholders have their number of shares reduced based on the terms of the stock split.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_date** | **datetime** | Date on which the stock split takes effect. | [optional] 
**ex_date** | **datetime** | The first date on which the shares will trade at the post-split price. | [optional] 
**units_ratio** | [**UnitsRatio**](UnitsRatio.md) |  | 
**record_date** | **datetime** | Date you have to be the holder of record in order to have their shares merged. | [optional] 
**announcement_date** | **datetime** | Date the reverse stock split was announced. | [optional] 
**fractional_units_cash_currency** | **str** | The currency of the cash paid in lieu of fractionalUnits. | [optional] 
**fractional_units_cash_price** | **float** | The cash price paid in lieu of fractionalUnits. | [optional] 
**instrument_event_type** | **str** | The Type of Event. The available values are: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent, ExpiryEvent, ScripDividendEvent, StockDividendEvent, ReverseStockSplitEvent, CapitalDistributionEvent, SpinOffEvent, MergerEvent, FutureExpiryEvent, SwapCashFlowEvent, SwapPrincipalEvent, CreditPremiumCashFlowEvent, CdsCreditEvent, CdxCreditEvent, MbsCouponEvent, MbsPrincipalEvent, BonusIssueEvent, MbsPrincipalWriteOffEvent, MbsInterestDeferralEvent, MbsInterestShortfallEvent, TenderEvent, CallOnIntermediateSecuritiesEvent, IntermediateSecuritiesDistributionEvent, OptionExercisePhysicalEvent, OptionExerciseCashEvent, ProtectionPayoutCashFlowEvent, TermDepositInterestEvent, TermDepositPrincipalEvent, EarlyRedemptionEvent, FutureMarkToMarketEvent, AdjustGlobalCommitmentEvent, ContractInitialisationEvent, DrawdownEvent, LoanInterestRepaymentEvent, UpdateDepositAmountEvent, LoanPrincipalRepaymentEvent, DepositInterestPaymentEvent, DepositCloseEvent, LoanFacilityContractRolloverEvent, RepurchaseOfferEvent, RepoPartialClosureEvent, RepoCashFlowEvent, FlexibleRepoInterestPaymentEvent, FlexibleRepoCashFlowEvent | 
## Example

```python
from lusid.models.reverse_stock_split_event import ReverseStockSplitEvent
from typing import Any, Dict, Optional, Union
from pydantic.v1 import Field, StrictFloat, StrictInt, StrictStr, validator
from datetime import datetime
payment_date: Optional[datetime] = # Replace with your value
ex_date: Optional[datetime] = # Replace with your value
units_ratio: UnitsRatio = # Replace with your value
record_date: Optional[datetime] = # Replace with your value
announcement_date: Optional[datetime] = # Replace with your value
fractional_units_cash_currency: Optional[StrictStr] = "example_fractional_units_cash_currency"
fractional_units_cash_price: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
instrument_event_type: StrictStr = "example_instrument_event_type"
reverse_stock_split_event_instance = ReverseStockSplitEvent(payment_date=payment_date, ex_date=ex_date, units_ratio=units_ratio, record_date=record_date, announcement_date=announcement_date, fractional_units_cash_currency=fractional_units_cash_currency, fractional_units_cash_price=fractional_units_cash_price, instrument_event_type=instrument_event_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

