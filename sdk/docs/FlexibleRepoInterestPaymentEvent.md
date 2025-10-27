# FlexibleRepoInterestPaymentEvent

Definition of FlexibleRepoInterestPaymentEvent, which represents the regular interest payments associated with an  open repo contract modelled as a FlexibleRepo.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**settlement_date** | **datetime** | Settlement date of the interest payment. This is a required field. | [optional] 
**entitlement_date** | **datetime** | EntitlementDate of the interest payment. This is a required field. | [optional] 
**currency** | **str** | Currency of the interest payment. This is a required field. | 
**interest_per_unit** | **float** | Interest payment per unit held of the FlexibleRepo. This field is optional. If not specified, the system  will not generate a virtual transaction for this event | [optional] 
**instrument_event_type** | **str** | The Type of Event. The available values are: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent, ExpiryEvent, ScripDividendEvent, StockDividendEvent, ReverseStockSplitEvent, CapitalDistributionEvent, SpinOffEvent, MergerEvent, FutureExpiryEvent, SwapCashFlowEvent, SwapPrincipalEvent, CreditPremiumCashFlowEvent, CdsCreditEvent, CdxCreditEvent, MbsCouponEvent, MbsPrincipalEvent, BonusIssueEvent, MbsPrincipalWriteOffEvent, MbsInterestDeferralEvent, MbsInterestShortfallEvent, TenderEvent, CallOnIntermediateSecuritiesEvent, IntermediateSecuritiesDistributionEvent, OptionExercisePhysicalEvent, OptionExerciseCashEvent, ProtectionPayoutCashFlowEvent, TermDepositInterestEvent, TermDepositPrincipalEvent, EarlyRedemptionEvent, FutureMarkToMarketEvent, AdjustGlobalCommitmentEvent, ContractInitialisationEvent, DrawdownEvent, LoanInterestRepaymentEvent, UpdateDepositAmountEvent, LoanPrincipalRepaymentEvent, DepositInterestPaymentEvent, DepositCloseEvent, LoanFacilityContractRolloverEvent, RepurchaseOfferEvent, RepoPartialClosureEvent, RepoCashFlowEvent, FlexibleRepoInterestPaymentEvent, FlexibleRepoCashFlowEvent, FlexibleRepoCollateralEvent, ConversionEvent, FlexibleRepoPartialClosureEvent, FlexibleRepoFullClosureEvent, CapletFloorletCashFlowEvent | 
## Example

```python
from lusid.models.flexible_repo_interest_payment_event import FlexibleRepoInterestPaymentEvent
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

settlement_date: Optional[datetime] = # Replace with your value
entitlement_date: Optional[datetime] = # Replace with your value
currency: StrictStr = "example_currency"
interest_per_unit: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
instrument_event_type: StrictStr = "example_instrument_event_type"
flexible_repo_interest_payment_event_instance = FlexibleRepoInterestPaymentEvent(settlement_date=settlement_date, entitlement_date=entitlement_date, currency=currency, interest_per_unit=interest_per_unit, instrument_event_type=instrument_event_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

