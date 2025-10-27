# LoanPrincipalRepaymentEvent

Event to signify the repayment of some or all of the principal balance of a loan contract.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_date** | **datetime** | Date that the Principal is due to be paid. | [optional] 
**currency** | **str** | Currency of the repayment. | 
**lapse_elections** | [**List[LapseElection]**](LapseElection.md) | Election for controlling whether the Principal is paid automatically or not.  Exactly one election must be provided. | [optional] 
**fraction** | **float** | Fraction of the outstanding settled principal balance to be repaid. Must be between 0 and 1, inclusive.  Defaults to 1 if not set. Ignored if the field Amount is set to a value different than zero. | [optional] 
**amount** | **float** | Amount to be repaid (independent of the fraction).  This field is not used at all if not set or set to 0, in this case the fraction field will be used instead.  Otherwise, the fraction field is ignored. | [optional] 
**with_interest** | **bool** | If set to true, then active contracts whose balance is reduced by the repayment will have  their accrued interest repaid proportionally to the balance reduction. | [optional] 
**instrument_event_type** | **str** | The Type of Event. The available values are: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent, ExpiryEvent, ScripDividendEvent, StockDividendEvent, ReverseStockSplitEvent, CapitalDistributionEvent, SpinOffEvent, MergerEvent, FutureExpiryEvent, SwapCashFlowEvent, SwapPrincipalEvent, CreditPremiumCashFlowEvent, CdsCreditEvent, CdxCreditEvent, MbsCouponEvent, MbsPrincipalEvent, BonusIssueEvent, MbsPrincipalWriteOffEvent, MbsInterestDeferralEvent, MbsInterestShortfallEvent, TenderEvent, CallOnIntermediateSecuritiesEvent, IntermediateSecuritiesDistributionEvent, OptionExercisePhysicalEvent, OptionExerciseCashEvent, ProtectionPayoutCashFlowEvent, TermDepositInterestEvent, TermDepositPrincipalEvent, EarlyRedemptionEvent, FutureMarkToMarketEvent, AdjustGlobalCommitmentEvent, ContractInitialisationEvent, DrawdownEvent, LoanInterestRepaymentEvent, UpdateDepositAmountEvent, LoanPrincipalRepaymentEvent, DepositInterestPaymentEvent, DepositCloseEvent, LoanFacilityContractRolloverEvent, RepurchaseOfferEvent, RepoPartialClosureEvent, RepoCashFlowEvent, FlexibleRepoInterestPaymentEvent, FlexibleRepoCashFlowEvent, FlexibleRepoCollateralEvent, ConversionEvent, FlexibleRepoPartialClosureEvent, FlexibleRepoFullClosureEvent, CapletFloorletCashFlowEvent | 
## Example

```python
from lusid.models.loan_principal_repayment_event import LoanPrincipalRepaymentEvent
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

payment_date: Optional[datetime] = # Replace with your value
currency: StrictStr = "example_currency"
lapse_elections: Optional[List[LapseElection]] = # Replace with your value
fraction: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
amount: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
with_interest: Optional[StrictBool] = # Replace with your value
with_interest:Optional[StrictBool] = None
instrument_event_type: StrictStr = "example_instrument_event_type"
loan_principal_repayment_event_instance = LoanPrincipalRepaymentEvent(payment_date=payment_date, currency=currency, lapse_elections=lapse_elections, fraction=fraction, amount=amount, with_interest=with_interest, instrument_event_type=instrument_event_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

