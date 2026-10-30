# CapitalInterestTransferEvent

The movement of a proportion of a CapitalInterest line's capital balances from one line to another.  The source (Out) side moves every balance by the fraction; the destination (In) side receives the  amounts given on the event. Mode distinguishes a genuine transfer between investors from a correction  of a mis-booked position. The portfolio-currency twin amounts (PaidInCapitalPortfolioCcyAmount,  ReturnedCapitalPortfolioCcyAmount and ExcessCapitalReturnedPortfolioCcyAmount) are not derived: an In side  that omits them books zero for the ...PortfolioCcy twins while the Out side gives up its share, and a  client-maintained transaction type configuration must include the ...PortfolioCcy twin movements for the  twins to move at all.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **datetime** | The date the transfer takes effect. | [optional] 
**direction** | **str** | Which side of the transfer this event books: &#39;Out&#39; on the source line or &#39;In&#39; on the destination line. Available values: Out, In. | 
**fraction** | **float** | The fraction of the source line being transferred. Must be greater than zero and at most one;  a fraction of one moves the whole line. | 
**from_line_id** | **str** | The identifier of the line the balances move from. | 
**to_line_id** | **str** | The identifier of the line the balances move to. | 
**mode** | **str** | &#39;Transfer&#39; for a genuine transfer between investors or &#39;Correction&#39; for a backdated fix of a  mis-booked position. Defaults to &#39;Transfer&#39;. Available values: Transfer, Correction. | [optional] 
**to_portfolio_id** | **str** | The identifier of the portfolio holding the destination line, if different from the source. | [optional] 
**consideration_amount** | **float** | The consideration paid for the transferred interest, if any. Must not be negative. | [optional] 
**consideration_currency** | **str** | The currency of the consideration, if any. | [optional] 
**consideration_record_only** | **bool** | True when the consideration is recorded for information only and does not settle. | [optional] 
**reason** | **str** | The reason for the transfer, if given: &#39;TaxStatusChange&#39;, &#39;Redomicile&#39;, &#39;SecondaryBuyerIneligible&#39;,  &#39;BenefitPlanLimit&#39;, &#39;WrongVehicleAtClose&#39;, &#39;AffiliateTransfer&#39;, &#39;Regulatory&#39;, &#39;VehicleMergerOrClosure&#39;,  &#39;NomineeUnwind&#39; or &#39;BlockerOrAivElection&#39;. Available values: None, TaxStatusChange, Redomicile, SecondaryBuyerIneligible, BenefitPlanLimit, WrongVehicleAtClose, AffiliateTransfer, Regulatory, VehicleMergerOrClosure, NomineeUnwind, BlockerOrAivElection. | [optional] 
**scope** | **str** | &#39;Whole&#39; to move the whole line or &#39;Deal&#39; to move only one deal&#39;s balances. &#39;Deal&#39; is only allowed  with reason &#39;BlockerOrAivElection&#39;. Defaults to &#39;Whole&#39;. Available values: Whole, Deal. | [optional] 
**deal_id** | **str** | The identifier of the deal the transfer relates to, if any. | [optional] 
**tax_treatment_acknowledged** | **bool** | Acknowledges that the tax treatment of a blocker or AIV election has been reviewed. Required to be  true when the reason is &#39;BlockerOrAivElection&#39;. | [optional] 
**committed_capital_amount** | **float** | The committed capital received by the destination line. Used on the &#39;In&#39; side only; must not be negative. | [optional] 
**called_commitment_amount** | **float** | The called part of the commitment received by the destination line, which lowers its uncalled commitment. Used on the &#39;In&#39; side only; must not be negative. | [optional] 
**paid_in_capital_amount** | **float** | The paid-in capital received by the destination line. Used on the &#39;In&#39; side only; must not be negative. | [optional] 
**returned_capital_amount** | **float** | The returned capital received by the destination line. Used on the &#39;In&#39; side only; must not be negative. | [optional] 
**recallable_capital_amount** | **float** | The recallable capital received by the destination line. Used on the &#39;In&#39; side only; must not be negative. | [optional] 
**non_recallable_capital_amount** | **float** | The non-recallable capital received by the destination line. Used on the &#39;In&#39; side only; must not be negative. | [optional] 
**funded_capital_amount** | **float** | The funded capital received by the destination line, for a line whose drawdowns were booked against the stored funded balance rather than paid-in capital. Used on the &#39;In&#39; side only; must not be negative. | [optional] 
**excess_capital_returned_amount** | **float** | The cumulative excess capital returned that the destination line takes over from the source line. Used on the &#39;In&#39; side only; must not be negative. | [optional] 
**paid_in_capital_portfolio_ccy_amount** | **float** | The paid-in capital the destination line takes over, already in the portfolio&#39;s base currency: the source line&#39;s PaidInCapitalPortfolioCcy balance share, accumulated at historical rates, not a spot conversion of PaidInCapitalAmount. Used on the &#39;In&#39; side only; must not be negative. An In side that omits it books zero for PaidInCapitalPortfolioCcy while the Out side gives up its share, and the transaction type configuration must include the PaidInCapitalPortfolioCcy movement for the twin to move. | [optional] 
**returned_capital_portfolio_ccy_amount** | **float** | The returned capital the destination line takes over, already in the portfolio&#39;s base currency at the source line&#39;s historical rates. Used on the &#39;In&#39; side only; must not be negative. An In side that omits it books zero for ReturnedCapitalPortfolioCcy while the Out side gives up its share, and the transaction type configuration must include the ReturnedCapitalPortfolioCcy movement for the twin to move. | [optional] 
**excess_capital_returned_portfolio_ccy_amount** | **float** | The cumulative excess capital returned that the destination line takes over, already in the portfolio&#39;s base currency at the source line&#39;s historical rates. Used on the &#39;In&#39; side only; must not be negative. An In side that omits it books zero for ExcessCapitalReturnedPortfolioCcy while the Out side gives up its share, and the transaction type configuration must include the ExcessCapitalReturnedPortfolioCcy movement for the twin to move. | [optional] 
**instrument_event_type** | **str** | The Type of Event. Available values: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent, ExpiryEvent, ScripDividendEvent, StockDividendEvent, ReverseStockSplitEvent, CapitalDistributionEvent, SpinOffEvent, MergerEvent, FutureExpiryEvent, SwapCashFlowEvent, SwapPrincipalEvent, CreditPremiumCashFlowEvent, CdsCreditEvent, CdxCreditEvent, MbsCouponEvent, MbsPrincipalEvent, BonusIssueEvent, MbsPrincipalWriteOffEvent, MbsInterestDeferralEvent, MbsInterestShortfallEvent, TenderEvent, CallOnIntermediateSecuritiesEvent, IntermediateSecuritiesDistributionEvent, OptionExercisePhysicalEvent, OptionExerciseCashEvent, ProtectionPayoutCashFlowEvent, TermDepositInterestEvent, TermDepositPrincipalEvent, EarlyRedemptionEvent, FutureMarkToMarketEvent, AdjustGlobalCommitmentEvent, ContractInitialisationEvent, DrawdownEvent, LoanInterestRepaymentEvent, UpdateDepositAmountEvent, LoanPrincipalRepaymentEvent, DepositInterestPaymentEvent, DepositCloseEvent, LoanFacilityContractRolloverEvent, RepurchaseOfferEvent, RepoPartialClosureEvent, RepoCashFlowEvent, FlexibleRepoInterestPaymentEvent, FlexibleRepoCashFlowEvent, FlexibleRepoCollateralEvent, ConversionEvent, FlexibleRepoPartialClosureEvent, FlexibleRepoFullClosureEvent, CapletFloorletCashFlowEvent, EarlyCloseOutEvent, DepositRollEvent, ConsentEvent, DrawingEvent, CapitalGainsDistributionEvent, ExchangeOfferEvent, DutchAuctionEvent, WorthlessEvent, PutRedemptionEvent, LoanFacilityDelayedCompensationPaymentEvent, InterestPaymentEvent, PriorityIssueEvent, ClassActionEvent, BankruptcyEvent, LiquidationPaymentEvent, PartialDefeasanceEvent, SecurityWriteOffEvent, WarrantsExerciseEvent, PariPassuEvent, ChangeEvent, PikBondCouponEvent, PikBondCashCouponEvent, PikBondInterestCapitalisationEvent, PikBondPrincipalEvent, DelistingEvent, PikBondInterestEvent, CommodityForwardCashSettlementEvent, PaymentInKindEvent, CommodityForwardPhysicalSettlementEvent, CancelSwapEvent, BondOptionTerminationEvent, TerminationEvent, CommodityCalendarSwapCashFlowEvent, DepositSweepEvent, BondForwardCashSettlementEvent, BondForwardTerminationEvent, AmendCommitmentEvent, CapitalCallEvent, FundDistributionEvent, NavReportEvent, DividendSuspensionEvent, LoanInterestCapitalisationEvent, TotalReturnSwapCashFlowEvent, GlobalLoanFacilityReinitialisationEvent, InvestorLoanFacilityReinitialisationEvent, CapitalCallReceiptEvent, RecallableCapitalExpiryEvent, CapitalInterestTransferEvent, FacilityDrawEvent, FacilityRepaymentEvent, FacilityInterestEvent, FacilityCommitmentFeeEvent, InstalmentCallEvent, DepositInterestCapitalisationEvent, PartialRedemptionWithoutReductionOfNominalValueEvent, StripBondCashflowEvent. | 
## Example

```python
from lusid.models.capital_interest_transfer_event import CapitalInterestTransferEvent
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

var_date: Optional[datetime] = # Replace with your value
direction: StrictStr = "example_direction"
fraction: Union[StrictFloat, StrictInt] = # Replace with your value
from_line_id: StrictStr = "example_from_line_id"
to_line_id: StrictStr = "example_to_line_id"
mode: Optional[StrictStr] = "example_mode"
to_portfolio_id: Optional[StrictStr] = "example_to_portfolio_id"
consideration_amount: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
consideration_currency: Optional[StrictStr] = "example_consideration_currency"
consideration_record_only: Optional[StrictBool] = # Replace with your value
consideration_record_only:Optional[StrictBool] = None
reason: Optional[StrictStr] = "example_reason"
scope: Optional[StrictStr] = "example_scope"
deal_id: Optional[StrictStr] = "example_deal_id"
tax_treatment_acknowledged: Optional[StrictBool] = # Replace with your value
tax_treatment_acknowledged:Optional[StrictBool] = None
committed_capital_amount: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
called_commitment_amount: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
paid_in_capital_amount: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
returned_capital_amount: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
recallable_capital_amount: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
non_recallable_capital_amount: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
funded_capital_amount: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
excess_capital_returned_amount: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
paid_in_capital_portfolio_ccy_amount: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
returned_capital_portfolio_ccy_amount: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
excess_capital_returned_portfolio_ccy_amount: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
instrument_event_type: StrictStr = "example_instrument_event_type"
capital_interest_transfer_event_instance = CapitalInterestTransferEvent(var_date=var_date, direction=direction, fraction=fraction, from_line_id=from_line_id, to_line_id=to_line_id, mode=mode, to_portfolio_id=to_portfolio_id, consideration_amount=consideration_amount, consideration_currency=consideration_currency, consideration_record_only=consideration_record_only, reason=reason, scope=scope, deal_id=deal_id, tax_treatment_acknowledged=tax_treatment_acknowledged, committed_capital_amount=committed_capital_amount, called_commitment_amount=called_commitment_amount, paid_in_capital_amount=paid_in_capital_amount, returned_capital_amount=returned_capital_amount, recallable_capital_amount=recallable_capital_amount, non_recallable_capital_amount=non_recallable_capital_amount, funded_capital_amount=funded_capital_amount, excess_capital_returned_amount=excess_capital_returned_amount, paid_in_capital_portfolio_ccy_amount=paid_in_capital_portfolio_ccy_amount, returned_capital_portfolio_ccy_amount=returned_capital_portfolio_ccy_amount, excess_capital_returned_portfolio_ccy_amount=excess_capital_returned_portfolio_ccy_amount, instrument_event_type=instrument_event_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

