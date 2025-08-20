# FlexibleRepoCashFlowEvent

Definition of FlexibleRepoCashFlowEvent which represents a cash transfer as part of a repo contract modelled as a FlexibleRepo, either as part of the purchase leg or repurchase leg, or any early closure.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**settlement_date** | **datetime** | Date that the cash payment settles. This is a required field. | [optional] 
**entitlement_date** | **datetime** | Date the recipient of the cash payment is entitled to receive the cash. This is a required field. | [optional] 
**currency** | **str** | Currency of the payment. This is a required field. | 
**cash_flow_per_unit** | **float** | Amount of cash to be paid per unit of the instrument. This amount is signed to indicate direction of the payment, i.e. as part of the purchase leg vs the repurchase leg. This field is optional. If not specified, the system will not generate a virtual transaction for this event. | [optional] 
**instrument_event_type** | **str** | The Type of Event. The available values are: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent, ExpiryEvent, ScripDividendEvent, StockDividendEvent, ReverseStockSplitEvent, CapitalDistributionEvent, SpinOffEvent, MergerEvent, FutureExpiryEvent, SwapCashFlowEvent, SwapPrincipalEvent, CreditPremiumCashFlowEvent, CdsCreditEvent, CdxCreditEvent, MbsCouponEvent, MbsPrincipalEvent, BonusIssueEvent, MbsPrincipalWriteOffEvent, MbsInterestDeferralEvent, MbsInterestShortfallEvent, TenderEvent, CallOnIntermediateSecuritiesEvent, IntermediateSecuritiesDistributionEvent, OptionExercisePhysicalEvent, OptionExerciseCashEvent, ProtectionPayoutCashFlowEvent, TermDepositInterestEvent, TermDepositPrincipalEvent, EarlyRedemptionEvent, FutureMarkToMarketEvent, AdjustGlobalCommitmentEvent, ContractInitialisationEvent, DrawdownEvent, LoanInterestRepaymentEvent, UpdateDepositAmountEvent, LoanPrincipalRepaymentEvent, DepositInterestPaymentEvent, DepositCloseEvent, LoanFacilityContractRolloverEvent, RepurchaseOfferEvent, RepoPartialClosureEvent, RepoCashFlowEvent, FlexibleRepoInterestPaymentEvent, FlexibleRepoCashFlowEvent, FlexibleRepoCollateralEvent, ConversionEvent, FlexibleRepoPartialClosureEvent, FlexibleRepoFullClosureEvent | 
## Example

```python
from lusid.models.flexible_repo_cash_flow_event import FlexibleRepoCashFlowEvent
from typing import Any, Dict, Optional, Union
from pydantic.v1 import Field, StrictFloat, StrictInt, StrictStr, validator
from datetime import datetime
settlement_date: Optional[datetime] = # Replace with your value
entitlement_date: Optional[datetime] = # Replace with your value
currency: StrictStr = "example_currency"
cash_flow_per_unit: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
instrument_event_type: StrictStr = "example_instrument_event_type"
flexible_repo_cash_flow_event_instance = FlexibleRepoCashFlowEvent(settlement_date=settlement_date, entitlement_date=entitlement_date, currency=currency, cash_flow_per_unit=cash_flow_per_unit, instrument_event_type=instrument_event_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

