# BondForwardCashSettlementEvent

Cash settlement of a BondForward at its settlement date:  the forward closes against a single net payment of the clean price difference, and no bond changes  hands. Unlike a commodity forward the underlying is a mastered, quoted instrument, so LUSID computes  the settlement amount from the underlying's quote rather than taking a pre-netted figure; a supplied  referencePrice wins and the quote is not consulted.  Accrued does not enter the payoff, by cancellation rather than entitlement: both sides of the  difference accrue to the same date, so the accrued is identical on each and drops out.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agreed_clean_price** | **float** | The agreed price, percent of par, carried from the definition. | 
**contract_size** | **float** | Face amount per unit, carried from the definition. It scales the payoff, so it is rejected where it  differs from the instrument&#39;s own value. | 
**maturity_date** | **datetime** | The forward&#39;s contractual settlement date, on which the price difference fixes. | [optional] 
**reference_price** | **float** | The underlying&#39;s clean price, percent of par, at the settlement date. Null resolves from the  underlying&#39;s quote; a supplied value wins and the quote is not consulted. | [optional] 
**settlement_amount_per_unit** | **float** | Output only: the net settlement per unit, computed from the reference price, the agreed price and  the contract size. A supplied value is overwritten. Negative is valid and means the holder pays. | [optional] 
**settlement_currency** | **str** | Currency the net amount settles in, being the forward&#39;s domestic currency. | 
**settlement_date** | **datetime** | The date the net payment settles. Null means the maturity date; cash-settled forwards commonly pay  a day or two after the price fixes. Rejected where earlier than the maturity date. | [optional] 
**instrument_event_type** | **str** | The Type of Event. Available values: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent, ExpiryEvent, ScripDividendEvent, StockDividendEvent, ReverseStockSplitEvent, CapitalDistributionEvent, SpinOffEvent, MergerEvent, FutureExpiryEvent, SwapCashFlowEvent, SwapPrincipalEvent, CreditPremiumCashFlowEvent, CdsCreditEvent, CdxCreditEvent, MbsCouponEvent, MbsPrincipalEvent, BonusIssueEvent, MbsPrincipalWriteOffEvent, MbsInterestDeferralEvent, MbsInterestShortfallEvent, TenderEvent, CallOnIntermediateSecuritiesEvent, IntermediateSecuritiesDistributionEvent, OptionExercisePhysicalEvent, OptionExerciseCashEvent, ProtectionPayoutCashFlowEvent, TermDepositInterestEvent, TermDepositPrincipalEvent, EarlyRedemptionEvent, FutureMarkToMarketEvent, AdjustGlobalCommitmentEvent, ContractInitialisationEvent, DrawdownEvent, LoanInterestRepaymentEvent, UpdateDepositAmountEvent, LoanPrincipalRepaymentEvent, DepositInterestPaymentEvent, DepositCloseEvent, LoanFacilityContractRolloverEvent, RepurchaseOfferEvent, RepoPartialClosureEvent, RepoCashFlowEvent, FlexibleRepoInterestPaymentEvent, FlexibleRepoCashFlowEvent, FlexibleRepoCollateralEvent, ConversionEvent, FlexibleRepoPartialClosureEvent, FlexibleRepoFullClosureEvent, CapletFloorletCashFlowEvent, EarlyCloseOutEvent, DepositRollEvent, ConsentEvent, DrawingEvent, CapitalGainsDistributionEvent, ExchangeOfferEvent, DutchAuctionEvent, WorthlessEvent, PutRedemptionEvent, LoanFacilityDelayedCompensationPaymentEvent, InterestPaymentEvent, PriorityIssueEvent, ClassActionEvent, BankruptcyEvent, LiquidationPaymentEvent, PartialDefeasanceEvent, SecurityWriteOffEvent, WarrantsExerciseEvent, PariPassuEvent, ChangeEvent, PikBondCouponEvent, PikBondCashCouponEvent, PikBondInterestCapitalisationEvent, PikBondPrincipalEvent, DelistingEvent, PikBondInterestEvent, CommodityForwardCashSettlementEvent, PaymentInKindEvent, CommodityForwardPhysicalSettlementEvent, CancelSwapEvent, BondOptionTerminationEvent, TerminationEvent, CommodityCalendarSwapCashFlowEvent, DepositSweepEvent, BondForwardCashSettlementEvent, BondForwardTerminationEvent, AmendCommitmentEvent, CapitalCallEvent, FundDistributionEvent, NavReportEvent. | 
## Example

```python
from lusid.models.bond_forward_cash_settlement_event import BondForwardCashSettlementEvent
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

agreed_clean_price: Union[StrictFloat, StrictInt] = # Replace with your value
contract_size: Union[StrictFloat, StrictInt] = # Replace with your value
maturity_date: Optional[datetime] = # Replace with your value
reference_price: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
settlement_amount_per_unit: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
settlement_currency: StrictStr = "example_settlement_currency"
settlement_date: Optional[datetime] = # Replace with your value
instrument_event_type: StrictStr = "example_instrument_event_type"
bond_forward_cash_settlement_event_instance = BondForwardCashSettlementEvent(agreed_clean_price=agreed_clean_price, contract_size=contract_size, maturity_date=maturity_date, reference_price=reference_price, settlement_amount_per_unit=settlement_amount_per_unit, settlement_currency=settlement_currency, settlement_date=settlement_date, instrument_event_type=instrument_event_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

