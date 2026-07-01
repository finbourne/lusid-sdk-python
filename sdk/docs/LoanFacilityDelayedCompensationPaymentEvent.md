# LoanFacilityDelayedCompensationPaymentEvent

event paying out the cumulative delayed-compensation pot on a secondary-market loan-facility  trade whose actual SettleDate is strictly after Transaction/default/ContractualSettlementDate. Generated  on the trade's actual SettleDate; amount equals the integrated daily increment over the open-on-the-left,  closed-on-the-right interval (ContractualSettlementDate, min(SettleDate, EarlyTerminationDate)].                Forecast accuracy depends entirely on the user's recorded SettleDate being a realistic estimate; if the  user fudges the settle date well into the future, the cashflow forecast will be wrong by the same factor.                Amount is always positive on the wire. Buyer-vs-seller sign is applied downstream by the transaction-template  specification, mirroring how BuyFacility / SellFacility already invert their cash legs against the same payload.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_date** | **datetime** | Date that the delayed-compensation pot is due to be paid. Kept as a separate field so a configurable  settlement-to-payment lag can be introduced later if the pot accrues using daily OIS rates; in the first  delivery PaymentDate equals ExDate. | [optional] 
**ex_date** | **datetime** | Date that the delayed-compensation pot is calculated up to. Equals the trade&#39;s actual SettleDate after  any active TradeAmendments at the firing effectiveAt. | [optional] 
**currency** | **str** | Currency of the payment, in the contract domestic currency. fx-conversion to the facility currency is  handled downstream in the same way as for LoanInterestRepaymentEvent. | 
**amount** | **float** | Cumulative pot value to be paid out on PaymentDate, expressed in the event&#39;s Currency. Always positive  on the wire; buyer-vs-seller sign is applied by the transaction-template specification per the original  trade side. | 
**instrument_event_type** | **str** | The Type of Event. Available values: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent, ExpiryEvent, ScripDividendEvent, StockDividendEvent, ReverseStockSplitEvent, CapitalDistributionEvent, SpinOffEvent, MergerEvent, FutureExpiryEvent, SwapCashFlowEvent, SwapPrincipalEvent, CreditPremiumCashFlowEvent, CdsCreditEvent, CdxCreditEvent, MbsCouponEvent, MbsPrincipalEvent, BonusIssueEvent, MbsPrincipalWriteOffEvent, MbsInterestDeferralEvent, MbsInterestShortfallEvent, TenderEvent, CallOnIntermediateSecuritiesEvent, IntermediateSecuritiesDistributionEvent, OptionExercisePhysicalEvent, OptionExerciseCashEvent, ProtectionPayoutCashFlowEvent, TermDepositInterestEvent, TermDepositPrincipalEvent, EarlyRedemptionEvent, FutureMarkToMarketEvent, AdjustGlobalCommitmentEvent, ContractInitialisationEvent, DrawdownEvent, LoanInterestRepaymentEvent, UpdateDepositAmountEvent, LoanPrincipalRepaymentEvent, DepositInterestPaymentEvent, DepositCloseEvent, LoanFacilityContractRolloverEvent, RepurchaseOfferEvent, RepoPartialClosureEvent, RepoCashFlowEvent, FlexibleRepoInterestPaymentEvent, FlexibleRepoCashFlowEvent, FlexibleRepoCollateralEvent, ConversionEvent, FlexibleRepoPartialClosureEvent, FlexibleRepoFullClosureEvent, CapletFloorletCashFlowEvent, EarlyCloseOutEvent, DepositRollEvent, ConsentEvent, DrawingEvent, CapitalGainsDistributionEvent, ExchangeOfferEvent, DutchAuctionEvent, WorthlessEvent, PutRedemptionEvent, LoanFacilityDelayedCompensationPaymentEvent, InterestPaymentEvent, PriorityIssueEvent, ClassActionEvent, BankruptcyEvent, LiquidationPaymentEvent, PartialDefeasanceEvent. | 
## Example

```python
from lusid.models.loan_facility_delayed_compensation_payment_event import LoanFacilityDelayedCompensationPaymentEvent
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

payment_date: Optional[datetime] = # Replace with your value
ex_date: Optional[datetime] = # Replace with your value
currency: StrictStr = "example_currency"
amount: Union[StrictFloat, StrictInt] = # Replace with your value
instrument_event_type: StrictStr = "example_instrument_event_type"
loan_facility_delayed_compensation_payment_event_instance = LoanFacilityDelayedCompensationPaymentEvent(payment_date=payment_date, ex_date=ex_date, currency=currency, amount=amount, instrument_event_type=instrument_event_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

