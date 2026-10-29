# CapitalCallReceiptEvent

The investor's payment against a capital call on a CapitalInterest. Booked separately from the call  because it arrives on a later date and may come in instalments; each populated slot books its own  receipt transaction so an unpaid fee never short-pays the deal.                The total amount may optionally be broken down into the same slots as the call (investment,  managementFee, otherFee, partnershipExpense, organisationalCost, recall, equalisationInterest,  latePaymentInterest). When any slot amount is supplied the slot amounts must sum to the total and  one transaction is booked per populated slot; otherwise a single receipt transaction is booked for  the total.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **datetime** | The date the receipt is paid. | [optional] 
**amount** | **float** | The total amount paid against the call. Must be positive. When slot amounts are supplied they  must sum to this total. | 
**call_event_id** | **str** | The identifier of the capital call event this receipt pays. | 
**investment_amount** | **float** | The part of the receipt that pays the investment slot of the call. Optional slot; must not be negative. | [optional] 
**management_fee_amount** | **float** | The part of the receipt that pays the management fee slot of the call. Optional slot; must not be negative. | [optional] 
**other_fee_amount** | **float** | The part of the receipt that pays the other fee slot of the call. Optional slot; must not be negative. | [optional] 
**partnership_expense_amount** | **float** | The part of the receipt that pays the partnership expense slot of the call. Optional slot; must not be negative. | [optional] 
**organisational_cost_amount** | **float** | The part of the receipt that pays the organisational cost slot of the call. Optional slot; must not be negative. | [optional] 
**recall_amount** | **float** | The part of the receipt that pays the recall slot of the call. Optional slot; must not be negative. | [optional] 
**equalisation_interest_amount** | **float** | The part of the receipt that pays the equalisation interest slot of the call. Optional slot; must not be negative. | [optional] 
**late_payment_interest_amount** | **float** | The part of the receipt that pays the late payment interest slot of the call. Optional slot; must not be negative. | [optional] 
**outside_commitment_slots** | **List[str]** | The slots (names without the Amount suffix, e.g. \&quot;managementFee\&quot;) that were called outside the  commitment, so that paying them does not move paid-in capital. When omitted, defaults to  equalisationInterest and latePaymentInterest. | [optional] 
**deal_id** | **str** | The identifier of the deal the receipt relates to, if any. | [optional] 
**allocation_event_id** | **str** | The identifier of the allocation event the receipt relates to, if any. | [optional] 
**instrument_event_type** | **str** | The Type of Event. Available values: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent, ExpiryEvent, ScripDividendEvent, StockDividendEvent, ReverseStockSplitEvent, CapitalDistributionEvent, SpinOffEvent, MergerEvent, FutureExpiryEvent, SwapCashFlowEvent, SwapPrincipalEvent, CreditPremiumCashFlowEvent, CdsCreditEvent, CdxCreditEvent, MbsCouponEvent, MbsPrincipalEvent, BonusIssueEvent, MbsPrincipalWriteOffEvent, MbsInterestDeferralEvent, MbsInterestShortfallEvent, TenderEvent, CallOnIntermediateSecuritiesEvent, IntermediateSecuritiesDistributionEvent, OptionExercisePhysicalEvent, OptionExerciseCashEvent, ProtectionPayoutCashFlowEvent, TermDepositInterestEvent, TermDepositPrincipalEvent, EarlyRedemptionEvent, FutureMarkToMarketEvent, AdjustGlobalCommitmentEvent, ContractInitialisationEvent, DrawdownEvent, LoanInterestRepaymentEvent, UpdateDepositAmountEvent, LoanPrincipalRepaymentEvent, DepositInterestPaymentEvent, DepositCloseEvent, LoanFacilityContractRolloverEvent, RepurchaseOfferEvent, RepoPartialClosureEvent, RepoCashFlowEvent, FlexibleRepoInterestPaymentEvent, FlexibleRepoCashFlowEvent, FlexibleRepoCollateralEvent, ConversionEvent, FlexibleRepoPartialClosureEvent, FlexibleRepoFullClosureEvent, CapletFloorletCashFlowEvent, EarlyCloseOutEvent, DepositRollEvent, ConsentEvent, DrawingEvent, CapitalGainsDistributionEvent, ExchangeOfferEvent, DutchAuctionEvent, WorthlessEvent, PutRedemptionEvent, LoanFacilityDelayedCompensationPaymentEvent, InterestPaymentEvent, PriorityIssueEvent, ClassActionEvent, BankruptcyEvent, LiquidationPaymentEvent, PartialDefeasanceEvent, SecurityWriteOffEvent, WarrantsExerciseEvent, PariPassuEvent, ChangeEvent, PikBondCouponEvent, PikBondCashCouponEvent, PikBondInterestCapitalisationEvent, PikBondPrincipalEvent, DelistingEvent, PikBondInterestEvent, CommodityForwardCashSettlementEvent, PaymentInKindEvent, CommodityForwardPhysicalSettlementEvent, CancelSwapEvent, BondOptionTerminationEvent, TerminationEvent, CommodityCalendarSwapCashFlowEvent, DepositSweepEvent, BondForwardCashSettlementEvent, BondForwardTerminationEvent, AmendCommitmentEvent, CapitalCallEvent, FundDistributionEvent, NavReportEvent, DividendSuspensionEvent, LoanInterestCapitalisationEvent, TotalReturnSwapCashFlowEvent, GlobalLoanFacilityReinitialisationEvent, InvestorLoanFacilityReinitialisationEvent, CapitalCallReceiptEvent, RecallableCapitalExpiryEvent, CapitalInterestTransferEvent, FacilityDrawEvent, FacilityRepaymentEvent, FacilityInterestEvent, FacilityCommitmentFeeEvent, InstalmentCallEvent, DepositInterestCapitalisationEvent, PartialRedemptionWithoutReductionOfNominalValueEvent. | 
## Example

```python
from lusid.models.capital_call_receipt_event import CapitalCallReceiptEvent
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

var_date: Optional[datetime] = # Replace with your value
amount: Union[StrictFloat, StrictInt] = # Replace with your value
call_event_id: StrictStr = "example_call_event_id"
investment_amount: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
management_fee_amount: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
other_fee_amount: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
partnership_expense_amount: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
organisational_cost_amount: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
recall_amount: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
equalisation_interest_amount: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
late_payment_interest_amount: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
outside_commitment_slots: Optional[List[StrictStr]] = # Replace with your value
deal_id: Optional[StrictStr] = "example_deal_id"
allocation_event_id: Optional[StrictStr] = "example_allocation_event_id"
instrument_event_type: StrictStr = "example_instrument_event_type"
capital_call_receipt_event_instance = CapitalCallReceiptEvent(var_date=var_date, amount=amount, call_event_id=call_event_id, investment_amount=investment_amount, management_fee_amount=management_fee_amount, other_fee_amount=other_fee_amount, partnership_expense_amount=partnership_expense_amount, organisational_cost_amount=organisational_cost_amount, recall_amount=recall_amount, equalisation_interest_amount=equalisation_interest_amount, late_payment_interest_amount=late_payment_interest_amount, outside_commitment_slots=outside_commitment_slots, deal_id=deal_id, allocation_event_id=allocation_event_id, instrument_event_type=instrument_event_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

