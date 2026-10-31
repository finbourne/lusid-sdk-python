# MbsPrincipalEvent

Definition of an MBS Principal Event  This is an event that describes the occurence of a cashflow due to a mortgage-backed security principal payment.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ex_date** | **datetime** | The ex date (entitlement date) of the principal payment, usually several weeks prior to the payment date | [optional] 
**payment_date** | **datetime** | The payment date of the principal | [optional] 
**currency** | **str** | The currency in which the principal is paid | 
**principal_per_unit** | **float** | The principal amount received for each unit of the instrument held on the ex date | [optional] 
**price_per_unit** | **float** | Redemption price per unit (OFFR / 100) of principal repaid. Clean price convention: a value of 1 is par.  Optional; a null is read as 1, so an omitted price is par. Separates the cash paid from the principal extinguished. | [optional] 
**previous_factor** | **float** | The pool factor in force until the redemption (factor) date, as notified (AMI-SeCo Previous Factor).  Optional; recorded for reconciliation and not consumed by the transaction template. Must be supplied together with nextFactor. | [optional] 
**next_factor** | **float** | The pool factor applicable after the redemption (factor) date, as notified (AMI-SeCo Next Factor).  Optional; recorded for reconciliation and not consumed by the transaction template. Must be supplied together with previousFactor. | [optional] 
**instrument_event_type** | **str** | The Type of Event. Available values: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent, ExpiryEvent, ScripDividendEvent, StockDividendEvent, ReverseStockSplitEvent, CapitalDistributionEvent, SpinOffEvent, MergerEvent, FutureExpiryEvent, SwapCashFlowEvent, SwapPrincipalEvent, CreditPremiumCashFlowEvent, CdsCreditEvent, CdxCreditEvent, MbsCouponEvent, MbsPrincipalEvent, BonusIssueEvent, MbsPrincipalWriteOffEvent, MbsInterestDeferralEvent, MbsInterestShortfallEvent, TenderEvent, CallOnIntermediateSecuritiesEvent, IntermediateSecuritiesDistributionEvent, OptionExercisePhysicalEvent, OptionExerciseCashEvent, ProtectionPayoutCashFlowEvent, TermDepositInterestEvent, TermDepositPrincipalEvent, EarlyRedemptionEvent, FutureMarkToMarketEvent, AdjustGlobalCommitmentEvent, ContractInitialisationEvent, DrawdownEvent, LoanInterestRepaymentEvent, UpdateDepositAmountEvent, LoanPrincipalRepaymentEvent, DepositInterestPaymentEvent, DepositCloseEvent, LoanFacilityContractRolloverEvent, RepurchaseOfferEvent, RepoPartialClosureEvent, RepoCashFlowEvent, FlexibleRepoInterestPaymentEvent, FlexibleRepoCashFlowEvent, FlexibleRepoCollateralEvent, ConversionEvent, FlexibleRepoPartialClosureEvent, FlexibleRepoFullClosureEvent, CapletFloorletCashFlowEvent, EarlyCloseOutEvent, DepositRollEvent, ConsentEvent, DrawingEvent, CapitalGainsDistributionEvent, ExchangeOfferEvent, DutchAuctionEvent, WorthlessEvent, PutRedemptionEvent, LoanFacilityDelayedCompensationPaymentEvent, InterestPaymentEvent, PriorityIssueEvent, ClassActionEvent, BankruptcyEvent, LiquidationPaymentEvent, PartialDefeasanceEvent, SecurityWriteOffEvent, WarrantsExerciseEvent, PariPassuEvent, ChangeEvent, PikBondCouponEvent, PikBondCashCouponEvent, PikBondInterestCapitalisationEvent, PikBondPrincipalEvent, DelistingEvent, PikBondInterestEvent, CommodityForwardCashSettlementEvent, PaymentInKindEvent, CommodityForwardPhysicalSettlementEvent, CancelSwapEvent, BondOptionTerminationEvent, TerminationEvent, CommodityCalendarSwapCashFlowEvent, DepositSweepEvent, BondForwardCashSettlementEvent, BondForwardTerminationEvent, AmendCommitmentEvent, CapitalCallEvent, FundDistributionEvent, NavReportEvent, DividendSuspensionEvent, LoanInterestCapitalisationEvent, TotalReturnSwapCashFlowEvent, GlobalLoanFacilityReinitialisationEvent, InvestorLoanFacilityReinitialisationEvent, CapitalCallReceiptEvent, RecallableCapitalExpiryEvent, CapitalInterestTransferEvent, FacilityDrawEvent, FacilityRepaymentEvent, FacilityInterestEvent, FacilityCommitmentFeeEvent, InstalmentCallEvent, DepositInterestCapitalisationEvent, PartialRedemptionWithoutReductionOfNominalValueEvent, StripBondCashflowEvent, CapitalisationEvent. | 
## Example

```python
from lusid.models.mbs_principal_event import MbsPrincipalEvent
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

ex_date: Optional[datetime] = # Replace with your value
payment_date: Optional[datetime] = # Replace with your value
currency: StrictStr = "example_currency"
principal_per_unit: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
price_per_unit: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
previous_factor: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
next_factor: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
instrument_event_type: StrictStr = "example_instrument_event_type"
mbs_principal_event_instance = MbsPrincipalEvent(ex_date=ex_date, payment_date=payment_date, currency=currency, principal_per_unit=principal_per_unit, price_per_unit=price_per_unit, previous_factor=previous_factor, next_factor=next_factor, instrument_event_type=instrument_event_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

