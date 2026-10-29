# PartialRedemptionWithoutReductionOfNominalValueEvent

Partial Redemption Without Reduction of Nominal Value (PRED, AMI-SeCo SCoRE section 4.47): securities are  redeemed in part before their scheduled final maturity date, the redemption is reflected in a pool factor  reduction and no movement of securities occurs. A notified PRED on an asset-backed ComplexBond. The holder  keeps its original face (units), the pool factor falls from previousFactor to nextFactor and the current face  falls with it; principalPerUnit of original face is repaid at pricePerUnit, par when omitted. Mandatory  participation only.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ex_date** | **datetime** | The entitlement date of the paydown. A PRED notification carries a record date (:98A::RDTE) and no ex-date;  the record date goes here. Required. | [optional] 
**payment_date** | **datetime** | The date the principal is paid and the date the next factor takes effect (:98A::PAYD). Required; on or  after exDate. | [optional] 
**currency** | **str** | The ISO 4217 code of the currency in which the principal is paid (:11A::OPTN). Required. | 
**principal_per_unit** | **float** | The principal repaid per unit of original face (AMI-SeCo RATE, per 1 of original face; a percentage is  divided by 100). Required and strictly positive. It may differ from previousFactor minus nextFactor,  because a write-off or an interest deferral in the same period moves the factor too. | [optional] 
**previous_factor** | **float** | The pool factor in force until paymentDate (:92A::PRFC). Required, together with nextFactor, so the  notified pool factor reduction can be reconciled against the custodian&#39;s factor file. | [optional] 
**next_factor** | **float** | The pool factor in force from paymentDate (:92A::NWFC). Required, together with previousFactor; strictly  positive and below previousFactor. | [optional] 
**price_per_unit** | **float** | The price per 1 of principal repaid (:90A::OFFR or :90B::OFFR), with 1 representing par; PRCT/98 is sent as  0.98. Optional; a null is read as 1, so an omitted price is par. | [optional] 
**instrument_event_type** | **str** | The Type of Event. Available values: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent, ExpiryEvent, ScripDividendEvent, StockDividendEvent, ReverseStockSplitEvent, CapitalDistributionEvent, SpinOffEvent, MergerEvent, FutureExpiryEvent, SwapCashFlowEvent, SwapPrincipalEvent, CreditPremiumCashFlowEvent, CdsCreditEvent, CdxCreditEvent, MbsCouponEvent, MbsPrincipalEvent, BonusIssueEvent, MbsPrincipalWriteOffEvent, MbsInterestDeferralEvent, MbsInterestShortfallEvent, TenderEvent, CallOnIntermediateSecuritiesEvent, IntermediateSecuritiesDistributionEvent, OptionExercisePhysicalEvent, OptionExerciseCashEvent, ProtectionPayoutCashFlowEvent, TermDepositInterestEvent, TermDepositPrincipalEvent, EarlyRedemptionEvent, FutureMarkToMarketEvent, AdjustGlobalCommitmentEvent, ContractInitialisationEvent, DrawdownEvent, LoanInterestRepaymentEvent, UpdateDepositAmountEvent, LoanPrincipalRepaymentEvent, DepositInterestPaymentEvent, DepositCloseEvent, LoanFacilityContractRolloverEvent, RepurchaseOfferEvent, RepoPartialClosureEvent, RepoCashFlowEvent, FlexibleRepoInterestPaymentEvent, FlexibleRepoCashFlowEvent, FlexibleRepoCollateralEvent, ConversionEvent, FlexibleRepoPartialClosureEvent, FlexibleRepoFullClosureEvent, CapletFloorletCashFlowEvent, EarlyCloseOutEvent, DepositRollEvent, ConsentEvent, DrawingEvent, CapitalGainsDistributionEvent, ExchangeOfferEvent, DutchAuctionEvent, WorthlessEvent, PutRedemptionEvent, LoanFacilityDelayedCompensationPaymentEvent, InterestPaymentEvent, PriorityIssueEvent, ClassActionEvent, BankruptcyEvent, LiquidationPaymentEvent, PartialDefeasanceEvent, SecurityWriteOffEvent, WarrantsExerciseEvent, PariPassuEvent, ChangeEvent, PikBondCouponEvent, PikBondCashCouponEvent, PikBondInterestCapitalisationEvent, PikBondPrincipalEvent, DelistingEvent, PikBondInterestEvent, CommodityForwardCashSettlementEvent, PaymentInKindEvent, CommodityForwardPhysicalSettlementEvent, CancelSwapEvent, BondOptionTerminationEvent, TerminationEvent, CommodityCalendarSwapCashFlowEvent, DepositSweepEvent, BondForwardCashSettlementEvent, BondForwardTerminationEvent, AmendCommitmentEvent, CapitalCallEvent, FundDistributionEvent, NavReportEvent, DividendSuspensionEvent, LoanInterestCapitalisationEvent, TotalReturnSwapCashFlowEvent, GlobalLoanFacilityReinitialisationEvent, InvestorLoanFacilityReinitialisationEvent, CapitalCallReceiptEvent, RecallableCapitalExpiryEvent, CapitalInterestTransferEvent, FacilityDrawEvent, FacilityRepaymentEvent, FacilityInterestEvent, FacilityCommitmentFeeEvent, InstalmentCallEvent, DepositInterestCapitalisationEvent, PartialRedemptionWithoutReductionOfNominalValueEvent. | 
## Example

```python
from lusid.models.partial_redemption_without_reduction_of_nominal_value_event import PartialRedemptionWithoutReductionOfNominalValueEvent
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

ex_date: Optional[datetime] = # Replace with your value
payment_date: Optional[datetime] = # Replace with your value
currency: StrictStr = "example_currency"
principal_per_unit: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
previous_factor: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
next_factor: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
price_per_unit: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
instrument_event_type: StrictStr = "example_instrument_event_type"
partial_redemption_without_reduction_of_nominal_value_event_instance = PartialRedemptionWithoutReductionOfNominalValueEvent(ex_date=ex_date, payment_date=payment_date, currency=currency, principal_per_unit=principal_per_unit, previous_factor=previous_factor, next_factor=next_factor, price_per_unit=price_per_unit, instrument_event_type=instrument_event_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

