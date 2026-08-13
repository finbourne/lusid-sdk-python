# CommodityForwardCashSettlementEvent

Cash settlement of a cash-delivery CommodityForward at maturity. The cash flow per unit is the  pre-netted settlement price (forward price minus strike) supplied externally via the quote store;  LUSID does not compute the difference itself. A negative cash flow per unit is valid and means the  position was out of the money at settlement.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**maturity_date** | **datetime** | The single settlement / maturity date of the forward. Required. | [optional] 
**dom_ccy** | **str** | Settlement currency of the forward. Required. | 
**cash_flow_per_unit** | **float** | The pre-netted settlement amount per unit (current forward price minus strike), supplied  externally via the quote store. Optional — absent until the settlement price has been loaded.  Negative when the position is out of the money. | [optional] 
**cash_flow_amount** | **float** | The realised cash amount, calculated as CashFlowPerUnit multiplied by the eligible balance.  Optional — it needs holdings-level data so it is never populated by the instrument layer.  Carries the sign of CashFlowPerUnit. | [optional] 
**strike** | **float** | Agreed forward price at trade inception. Optional, and reference only — it is not used in the  settlement calculation; it is carried for auditability. | [optional] 
**instrument_event_type** | **str** | The Type of Event. Available values: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent, ExpiryEvent, ScripDividendEvent, StockDividendEvent, ReverseStockSplitEvent, CapitalDistributionEvent, SpinOffEvent, MergerEvent, FutureExpiryEvent, SwapCashFlowEvent, SwapPrincipalEvent, CreditPremiumCashFlowEvent, CdsCreditEvent, CdxCreditEvent, MbsCouponEvent, MbsPrincipalEvent, BonusIssueEvent, MbsPrincipalWriteOffEvent, MbsInterestDeferralEvent, MbsInterestShortfallEvent, TenderEvent, CallOnIntermediateSecuritiesEvent, IntermediateSecuritiesDistributionEvent, OptionExercisePhysicalEvent, OptionExerciseCashEvent, ProtectionPayoutCashFlowEvent, TermDepositInterestEvent, TermDepositPrincipalEvent, EarlyRedemptionEvent, FutureMarkToMarketEvent, AdjustGlobalCommitmentEvent, ContractInitialisationEvent, DrawdownEvent, LoanInterestRepaymentEvent, UpdateDepositAmountEvent, LoanPrincipalRepaymentEvent, DepositInterestPaymentEvent, DepositCloseEvent, LoanFacilityContractRolloverEvent, RepurchaseOfferEvent, RepoPartialClosureEvent, RepoCashFlowEvent, FlexibleRepoInterestPaymentEvent, FlexibleRepoCashFlowEvent, FlexibleRepoCollateralEvent, ConversionEvent, FlexibleRepoPartialClosureEvent, FlexibleRepoFullClosureEvent, CapletFloorletCashFlowEvent, EarlyCloseOutEvent, DepositRollEvent, ConsentEvent, DrawingEvent, CapitalGainsDistributionEvent, ExchangeOfferEvent, DutchAuctionEvent, WorthlessEvent, PutRedemptionEvent, LoanFacilityDelayedCompensationPaymentEvent, InterestPaymentEvent, PriorityIssueEvent, ClassActionEvent, BankruptcyEvent, LiquidationPaymentEvent, PartialDefeasanceEvent, SecurityWriteOffEvent, WarrantsExerciseEvent, PariPassuEvent, ChangeEvent, PikBondCouponEvent, PikBondCashCouponEvent, PikBondInterestCapitalisationEvent, PikBondPrincipalEvent, DelistingEvent, PikBondInterestEvent, CommodityForwardCashSettlementEvent. | 
## Example

```python
from lusid.models.commodity_forward_cash_settlement_event import CommodityForwardCashSettlementEvent
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

maturity_date: Optional[datetime] = # Replace with your value
dom_ccy: StrictStr = "example_dom_ccy"
cash_flow_per_unit: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
cash_flow_amount: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
strike: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
instrument_event_type: StrictStr = "example_instrument_event_type"
commodity_forward_cash_settlement_event_instance = CommodityForwardCashSettlementEvent(maturity_date=maturity_date, dom_ccy=dom_ccy, cash_flow_per_unit=cash_flow_per_unit, cash_flow_amount=cash_flow_amount, strike=strike, instrument_event_type=instrument_event_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

