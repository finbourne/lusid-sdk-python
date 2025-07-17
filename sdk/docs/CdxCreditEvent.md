# CdxCreditEvent

Definition of a credit event for credit default swap index (CDX) instruments.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**effective_date** | **datetime** | The date of the credit default - i.e. date on which the debt issuer defaulted on its repayment obligation. | [optional] 
**auction_date** | **datetime** | The date of the credit event auction - i.e. date on which the defaulted debt is sold via auction, and a recovery rate determined. | [optional] 
**recovery_rate** | **float** | The fraction of the defaulted debt that can be recovered. | [optional] 
**constituent_weight** | **float** | The relative weight of the CDX constituent. | 
**constituent_reference** | **str** | Reference value used to identify the CDX constituent. | [optional] 
**payment_date** | **datetime** | The date of the credit event auction settlement. | [optional] 
**instrument_event_type** | **str** | The Type of Event. The available values are: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent, ExpiryEvent, ScripDividendEvent, StockDividendEvent, ReverseStockSplitEvent, CapitalDistributionEvent, SpinOffEvent, MergerEvent, FutureExpiryEvent, SwapCashFlowEvent, SwapPrincipalEvent, CreditPremiumCashFlowEvent, CdsCreditEvent, CdxCreditEvent, MbsCouponEvent, MbsPrincipalEvent, BonusIssueEvent, MbsPrincipalWriteOffEvent, MbsInterestDeferralEvent, MbsInterestShortfallEvent, TenderEvent, CallOnIntermediateSecuritiesEvent, IntermediateSecuritiesDistributionEvent, OptionExercisePhysicalEvent, OptionExerciseCashEvent, ProtectionPayoutCashFlowEvent, TermDepositInterestEvent, TermDepositPrincipalEvent, EarlyRedemptionEvent, FutureMarkToMarketEvent, AdjustGlobalCommitmentEvent, ContractInitialisationEvent, DrawdownEvent, LoanInterestRepaymentEvent, UpdateDepositAmountEvent, LoanPrincipalRepaymentEvent, DepositInterestPaymentEvent, DepositCloseEvent, LoanFacilityContractRolloverEvent, RepurchaseOfferEvent, RepoPartialClosureEvent, RepoCashFlowEvent, FlexibleRepoInterestPaymentEvent, FlexibleRepoCashFlowEvent, FlexibleRepoCollateralEvent | 
## Example

```python
from lusid.models.cdx_credit_event import CdxCreditEvent
from typing import Any, Dict, Optional, Union
from pydantic.v1 import Field, StrictFloat, StrictInt, StrictStr, validator
from datetime import datetime
effective_date: Optional[datetime] = # Replace with your value
auction_date: Optional[datetime] = # Replace with your value
recovery_rate: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
constituent_weight: Union[StrictFloat, StrictInt] = # Replace with your value
constituent_reference: Optional[StrictStr] = "example_constituent_reference"
payment_date: Optional[datetime] = # Replace with your value
instrument_event_type: StrictStr = "example_instrument_event_type"
cdx_credit_event_instance = CdxCreditEvent(effective_date=effective_date, auction_date=auction_date, recovery_rate=recovery_rate, constituent_weight=constituent_weight, constituent_reference=constituent_reference, payment_date=payment_date, instrument_event_type=instrument_event_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

