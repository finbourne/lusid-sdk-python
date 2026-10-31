# FundDistributionEvent

A distribution from the fund to the holder of a CapitalInterest. A recallable distribution restores  unfunded capital (the fund may call it again); a non-recallable distribution permanently returns capital.                The total amount may optionally be broken down into slots by character (returnOfCapital, realisedGain,  dividend, interest, otherIncome, carryPaid, withholding, returnOfExcess). When any slot amount is supplied  the slot amounts must sum to the total, one transaction is booked per populated slot, and the recallable  portion of each of the five capital/income characters is given by its matching Recallable amount.  Without slots a single legacy distribution transaction is booked for the total, recallable according  to isRecallable.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **datetime** | The date the distribution takes effect. | [optional] 
**amount** | **float** | The total amount distributed. Must be positive. When slot amounts are supplied they must sum to this total. | 
**is_recallable** | **bool** | Legacy flag, used only when no slot amount is supplied: true when the fund may recall the whole  distributed amount, so the distribution restores unfunded capital rather than permanently returning  it. Defaults to false. Must not be combined with slot amounts. | [optional] 
**return_of_capital_amount** | **float** | The part of the distribution that returns capital. Optional slot; must not be negative. | [optional] 
**realised_gain_amount** | **float** | The part of the distribution that is realised gain. Optional slot; must not be negative. | [optional] 
**dividend_amount** | **float** | The part of the distribution that is dividend income. Optional slot; must not be negative. | [optional] 
**interest_amount** | **float** | The part of the distribution that is interest income. Optional slot; must not be negative. | [optional] 
**other_income_amount** | **float** | The part of the distribution that is other income. Optional slot; must not be negative. | [optional] 
**return_of_capital_recallable_amount** | **float** | The recallable portion of returnOfCapitalAmount. Optional; must not exceed returnOfCapitalAmount. | [optional] 
**realised_gain_recallable_amount** | **float** | The recallable portion of realisedGainAmount. Optional; must not exceed realisedGainAmount. | [optional] 
**dividend_recallable_amount** | **float** | The recallable portion of dividendAmount. Optional; must not exceed dividendAmount. | [optional] 
**interest_recallable_amount** | **float** | The recallable portion of interestAmount. Optional; must not exceed interestAmount. | [optional] 
**other_income_recallable_amount** | **float** | The recallable portion of otherIncomeAmount. Optional; must not exceed otherIncomeAmount. | [optional] 
**carry_paid_amount** | **float** | The part of the distribution that is carried interest paid to the general partner. Optional slot; must not be negative. | [optional] 
**withholding_amount** | **float** | The part of the distribution withheld for tax (a deemed distribution). Optional slot; must not be negative. | [optional] 
**return_of_excess_amount** | **float** | The part of the distribution that returns capital called in excess. Optional slot; must not be negative. | [optional] 
**recallable_until** | **datetime** | The date until which the recallable portions may be recalled, if limited. Must not precede the distribution date. | [optional] 
**deal_id** | **str** | The identifier of the deal the distribution relates to, if any. | [optional] 
**allocation_event_id** | **str** | The identifier of the allocation event the distribution relates to, if any. | [optional] 
**waterfall_tier** | **str** | The waterfall tier the distribution was paid under, if any. | [optional] 
**instrument_event_type** | **str** | The Type of Event. Available values: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent, ExpiryEvent, ScripDividendEvent, StockDividendEvent, ReverseStockSplitEvent, CapitalDistributionEvent, SpinOffEvent, MergerEvent, FutureExpiryEvent, SwapCashFlowEvent, SwapPrincipalEvent, CreditPremiumCashFlowEvent, CdsCreditEvent, CdxCreditEvent, MbsCouponEvent, MbsPrincipalEvent, BonusIssueEvent, MbsPrincipalWriteOffEvent, MbsInterestDeferralEvent, MbsInterestShortfallEvent, TenderEvent, CallOnIntermediateSecuritiesEvent, IntermediateSecuritiesDistributionEvent, OptionExercisePhysicalEvent, OptionExerciseCashEvent, ProtectionPayoutCashFlowEvent, TermDepositInterestEvent, TermDepositPrincipalEvent, EarlyRedemptionEvent, FutureMarkToMarketEvent, AdjustGlobalCommitmentEvent, ContractInitialisationEvent, DrawdownEvent, LoanInterestRepaymentEvent, UpdateDepositAmountEvent, LoanPrincipalRepaymentEvent, DepositInterestPaymentEvent, DepositCloseEvent, LoanFacilityContractRolloverEvent, RepurchaseOfferEvent, RepoPartialClosureEvent, RepoCashFlowEvent, FlexibleRepoInterestPaymentEvent, FlexibleRepoCashFlowEvent, FlexibleRepoCollateralEvent, ConversionEvent, FlexibleRepoPartialClosureEvent, FlexibleRepoFullClosureEvent, CapletFloorletCashFlowEvent, EarlyCloseOutEvent, DepositRollEvent, ConsentEvent, DrawingEvent, CapitalGainsDistributionEvent, ExchangeOfferEvent, DutchAuctionEvent, WorthlessEvent, PutRedemptionEvent, LoanFacilityDelayedCompensationPaymentEvent, InterestPaymentEvent, PriorityIssueEvent, ClassActionEvent, BankruptcyEvent, LiquidationPaymentEvent, PartialDefeasanceEvent, SecurityWriteOffEvent, WarrantsExerciseEvent, PariPassuEvent, ChangeEvent, PikBondCouponEvent, PikBondCashCouponEvent, PikBondInterestCapitalisationEvent, PikBondPrincipalEvent, DelistingEvent, PikBondInterestEvent, CommodityForwardCashSettlementEvent, PaymentInKindEvent, CommodityForwardPhysicalSettlementEvent, CancelSwapEvent, BondOptionTerminationEvent, TerminationEvent, CommodityCalendarSwapCashFlowEvent, DepositSweepEvent, BondForwardCashSettlementEvent, BondForwardTerminationEvent, AmendCommitmentEvent, CapitalCallEvent, FundDistributionEvent, NavReportEvent, DividendSuspensionEvent, LoanInterestCapitalisationEvent, TotalReturnSwapCashFlowEvent, GlobalLoanFacilityReinitialisationEvent, InvestorLoanFacilityReinitialisationEvent, CapitalCallReceiptEvent, RecallableCapitalExpiryEvent, CapitalInterestTransferEvent, FacilityDrawEvent, FacilityRepaymentEvent, FacilityInterestEvent, FacilityCommitmentFeeEvent, InstalmentCallEvent, DepositInterestCapitalisationEvent, PartialRedemptionWithoutReductionOfNominalValueEvent, StripBondCashflowEvent, CapitalisationEvent. | 
## Example

```python
from lusid.models.fund_distribution_event import FundDistributionEvent
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

var_date: Optional[datetime] = # Replace with your value
amount: Union[StrictFloat, StrictInt] = # Replace with your value
is_recallable: Optional[StrictBool] = # Replace with your value
is_recallable:Optional[StrictBool] = None
return_of_capital_amount: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
realised_gain_amount: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
dividend_amount: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
interest_amount: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
other_income_amount: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
return_of_capital_recallable_amount: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
realised_gain_recallable_amount: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
dividend_recallable_amount: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
interest_recallable_amount: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
other_income_recallable_amount: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
carry_paid_amount: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
withholding_amount: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
return_of_excess_amount: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
recallable_until: Optional[datetime] = # Replace with your value
deal_id: Optional[StrictStr] = "example_deal_id"
allocation_event_id: Optional[StrictStr] = "example_allocation_event_id"
waterfall_tier: Optional[StrictStr] = "example_waterfall_tier"
instrument_event_type: StrictStr = "example_instrument_event_type"
fund_distribution_event_instance = FundDistributionEvent(var_date=var_date, amount=amount, is_recallable=is_recallable, return_of_capital_amount=return_of_capital_amount, realised_gain_amount=realised_gain_amount, dividend_amount=dividend_amount, interest_amount=interest_amount, other_income_amount=other_income_amount, return_of_capital_recallable_amount=return_of_capital_recallable_amount, realised_gain_recallable_amount=realised_gain_recallable_amount, dividend_recallable_amount=dividend_recallable_amount, interest_recallable_amount=interest_recallable_amount, other_income_recallable_amount=other_income_recallable_amount, carry_paid_amount=carry_paid_amount, withholding_amount=withholding_amount, return_of_excess_amount=return_of_excess_amount, recallable_until=recallable_until, deal_id=deal_id, allocation_event_id=allocation_event_id, waterfall_tier=waterfall_tier, instrument_event_type=instrument_event_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

