# EarlyCloseOutEvent

Early close out event - Ending an OTC instrument early.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**close_out_amount** | **float** | The amount to be closed out early. Required. Must be strictly positive. | 
**close_out_ccy** | **str** | The currency corresponding to the amount to be closed out early. Required. | 
**close_out_to_other_rate** | **float** | The rate between close out amount and other amount. Optional. If provided, must be strictly positive. | [optional] 
**effective_date** | **datetime** | The date of the event. | [optional] 
**other_amount** | **float** | The other amount to be closed out early. Optional. If provided, must be strictly positive. | [optional] 
**other_ccy** | **str** | The currency corresponding to the other amount to be closed out early. Optional. | [optional] 
**other_to_close_out_rate** | **float** | The rate between other amount and close out amount. Optional. If provided, must be strictly positive. | [optional] 
**settlement_ccy** | **str** | The settlement currency. Required. | 
**instrument_event_type** | **str** | The Type of Event. The available values are: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent, ExpiryEvent, ScripDividendEvent, StockDividendEvent, ReverseStockSplitEvent, CapitalDistributionEvent, SpinOffEvent, MergerEvent, FutureExpiryEvent, SwapCashFlowEvent, SwapPrincipalEvent, CreditPremiumCashFlowEvent, CdsCreditEvent, CdxCreditEvent, MbsCouponEvent, MbsPrincipalEvent, BonusIssueEvent, MbsPrincipalWriteOffEvent, MbsInterestDeferralEvent, MbsInterestShortfallEvent, TenderEvent, CallOnIntermediateSecuritiesEvent, IntermediateSecuritiesDistributionEvent, OptionExercisePhysicalEvent, OptionExerciseCashEvent, ProtectionPayoutCashFlowEvent, TermDepositInterestEvent, TermDepositPrincipalEvent, EarlyRedemptionEvent, FutureMarkToMarketEvent, AdjustGlobalCommitmentEvent, ContractInitialisationEvent, DrawdownEvent, LoanInterestRepaymentEvent, UpdateDepositAmountEvent, LoanPrincipalRepaymentEvent, DepositInterestPaymentEvent, DepositCloseEvent, LoanFacilityContractRolloverEvent, RepurchaseOfferEvent, RepoPartialClosureEvent, RepoCashFlowEvent, FlexibleRepoInterestPaymentEvent, FlexibleRepoCashFlowEvent, FlexibleRepoCollateralEvent, ConversionEvent, FlexibleRepoPartialClosureEvent, FlexibleRepoFullClosureEvent, CapletFloorletCashFlowEvent, EarlyCloseOutEvent | 
## Example

```python
from lusid.models.early_close_out_event import EarlyCloseOutEvent
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

close_out_amount: Union[StrictFloat, StrictInt] = # Replace with your value
close_out_ccy: StrictStr = "example_close_out_ccy"
close_out_to_other_rate: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
effective_date: Optional[datetime] = # Replace with your value
other_amount: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
other_ccy: Optional[StrictStr] = "example_other_ccy"
other_to_close_out_rate: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
settlement_ccy: StrictStr = "example_settlement_ccy"
instrument_event_type: StrictStr = "example_instrument_event_type"
early_close_out_event_instance = EarlyCloseOutEvent(close_out_amount=close_out_amount, close_out_ccy=close_out_ccy, close_out_to_other_rate=close_out_to_other_rate, effective_date=effective_date, other_amount=other_amount, other_ccy=other_ccy, other_to_close_out_rate=other_to_close_out_rate, settlement_ccy=settlement_ccy, instrument_event_type=instrument_event_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

