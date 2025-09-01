# FlexibleRepoPartialClosureEvent

Event representing the partial closure of a repurchase   agreement. Each event reduces the outstanding notional   and generates a corresponding receive-leg cashflow. The   final maturity cashflow is adjusted accordingly.  If multiple events are created, their effects compound.   Once the total repaid amount reaches the original purchase   price, no further receive-leg cashflows are generated. Any   event exceeding the remaining notional is marked with a   diagnostic to indicate it is invalid due to excessive repayment.  For example, for a repo with a 5% rate, 1% haircut and   collateral value of 100 (purchase price = 99), a partial   closure of cash amount 10 followed by one of 100 results in   only the first event producing a cashflow. The second,   exceeding the remaining balance, is ignored and flagged   with a diagnostic. The remaining balance is settled at   maturity of the repurchase agreement.  Specific to a  instrument.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entitlement_date** | **datetime** | Required property.  The date on which the counterparties become entitled   to exchange cash as part of a partial closure of the   repurchase agreement. The date must be before or on   the settlement date, and on or before the maturity   date of the repo. | [optional] 
**settlement_date** | **datetime** | Required property.  The date on which the exchange of cash is settled.   The date must be on or after the entitlement date,  and on or before the maturity date of the repo. | [optional] 
**amount** | **float** | The amount of cash to be exchanged as part of a partial closure of the repurchase agreement.  Either the absolute cash amount or a percentage of the remaining amount,  depending on the AmountType. | 
**amount_type** | **str** | AmountType of the cash amount to be exchanged as part of a partial closure of the repurchase agreement.  Either percentage or absolute cash amount.    Supported string (enumeration) values are: [Percentage, Units]. | 
**partial_closure_constituents** | [**List[PartialClosureConstituent]**](PartialClosureConstituent.md) | List of the collateral instruments involved in this partial closure, along with how they are affected. | 
**instrument_event_type** | **str** | The Type of Event. The available values are: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent, ExpiryEvent, ScripDividendEvent, StockDividendEvent, ReverseStockSplitEvent, CapitalDistributionEvent, SpinOffEvent, MergerEvent, FutureExpiryEvent, SwapCashFlowEvent, SwapPrincipalEvent, CreditPremiumCashFlowEvent, CdsCreditEvent, CdxCreditEvent, MbsCouponEvent, MbsPrincipalEvent, BonusIssueEvent, MbsPrincipalWriteOffEvent, MbsInterestDeferralEvent, MbsInterestShortfallEvent, TenderEvent, CallOnIntermediateSecuritiesEvent, IntermediateSecuritiesDistributionEvent, OptionExercisePhysicalEvent, OptionExerciseCashEvent, ProtectionPayoutCashFlowEvent, TermDepositInterestEvent, TermDepositPrincipalEvent, EarlyRedemptionEvent, FutureMarkToMarketEvent, AdjustGlobalCommitmentEvent, ContractInitialisationEvent, DrawdownEvent, LoanInterestRepaymentEvent, UpdateDepositAmountEvent, LoanPrincipalRepaymentEvent, DepositInterestPaymentEvent, DepositCloseEvent, LoanFacilityContractRolloverEvent, RepurchaseOfferEvent, RepoPartialClosureEvent, RepoCashFlowEvent, FlexibleRepoInterestPaymentEvent, FlexibleRepoCashFlowEvent, FlexibleRepoCollateralEvent, ConversionEvent, FlexibleRepoPartialClosureEvent, FlexibleRepoFullClosureEvent, CapletFloorletCashFlowEvent | 
## Example

```python
from lusid.models.flexible_repo_partial_closure_event import FlexibleRepoPartialClosureEvent
from typing import Any, Dict, List, Optional, Union
from pydantic.v1 import Field, StrictFloat, StrictInt, StrictStr, conlist, constr, validator
from datetime import datetime
entitlement_date: Optional[datetime] = # Replace with your value
settlement_date: Optional[datetime] = # Replace with your value
amount: Union[StrictFloat, StrictInt] = # Replace with your value
amount_type: StrictStr = "example_amount_type"
partial_closure_constituents: conlist(PartialClosureConstituent) = # Replace with your value
instrument_event_type: StrictStr = "example_instrument_event_type"
flexible_repo_partial_closure_event_instance = FlexibleRepoPartialClosureEvent(entitlement_date=entitlement_date, settlement_date=settlement_date, amount=amount, amount_type=amount_type, partial_closure_constituents=partial_closure_constituents, instrument_event_type=instrument_event_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

