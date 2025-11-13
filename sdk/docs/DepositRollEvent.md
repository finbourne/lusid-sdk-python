# DepositRollEvent

Event used to represent a roll on a FlexibleDeposit instrument.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entitlement_date** | **datetime** | The entitlement date of the roll event. | [optional] 
**settlement_date** | **datetime** | The settlement date of the roll event. | [optional] 
**principal_updates** | [**RollPrincipalUpdates**](RollPrincipalUpdates.md) |  | 
**interest_updates** | [**RollInterestUpdates**](RollInterestUpdates.md) |  | 
**new_schedule** | [**Schedule**](Schedule.md) |  | [optional] 
**instrument_event_type** | **str** | The Type of Event. The available values are: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent, ExpiryEvent, ScripDividendEvent, StockDividendEvent, ReverseStockSplitEvent, CapitalDistributionEvent, SpinOffEvent, MergerEvent, FutureExpiryEvent, SwapCashFlowEvent, SwapPrincipalEvent, CreditPremiumCashFlowEvent, CdsCreditEvent, CdxCreditEvent, MbsCouponEvent, MbsPrincipalEvent, BonusIssueEvent, MbsPrincipalWriteOffEvent, MbsInterestDeferralEvent, MbsInterestShortfallEvent, TenderEvent, CallOnIntermediateSecuritiesEvent, IntermediateSecuritiesDistributionEvent, OptionExercisePhysicalEvent, OptionExerciseCashEvent, ProtectionPayoutCashFlowEvent, TermDepositInterestEvent, TermDepositPrincipalEvent, EarlyRedemptionEvent, FutureMarkToMarketEvent, AdjustGlobalCommitmentEvent, ContractInitialisationEvent, DrawdownEvent, LoanInterestRepaymentEvent, UpdateDepositAmountEvent, LoanPrincipalRepaymentEvent, DepositInterestPaymentEvent, DepositCloseEvent, LoanFacilityContractRolloverEvent, RepurchaseOfferEvent, RepoPartialClosureEvent, RepoCashFlowEvent, FlexibleRepoInterestPaymentEvent, FlexibleRepoCashFlowEvent, FlexibleRepoCollateralEvent, ConversionEvent, FlexibleRepoPartialClosureEvent, FlexibleRepoFullClosureEvent, CapletFloorletCashFlowEvent, EarlyCloseOutEvent, DepositRollEvent | 
## Example

```python
from lusid.models.deposit_roll_event import DepositRollEvent
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

entitlement_date: Optional[datetime] = # Replace with your value
settlement_date: Optional[datetime] = # Replace with your value
principal_updates: RollPrincipalUpdates = # Replace with your value
interest_updates: RollInterestUpdates = # Replace with your value
new_schedule: Optional[Schedule] = # Replace with your value
instrument_event_type: StrictStr = "example_instrument_event_type"
deposit_roll_event_instance = DepositRollEvent(entitlement_date=entitlement_date, settlement_date=settlement_date, principal_updates=principal_updates, interest_updates=interest_updates, new_schedule=new_schedule, instrument_event_type=instrument_event_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

