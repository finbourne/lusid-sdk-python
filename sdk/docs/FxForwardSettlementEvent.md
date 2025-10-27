# FxForwardSettlementEvent

Settlement for FX Forward, including NDF and deliverable.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**maturity_date** | **datetime** | Maturity date of the forward | [optional] 
**dom_amount_per_unit** | **float** | Amount per unit in the DomCcy (domestic currency) | 
**dom_ccy** | **str** | The domestic currency of the forward | 
**fgn_amount_per_unit** | **float** | Amount per unit in the FgnCcy (foreign currency) | 
**fgn_ccy** | **str** | The foreign currency of the forward. | 
**is_ndf** | **bool** | Is this settlement corresponding to a deliverable forward, or an NDF | 
**fixing_date** | **datetime** | Optional.  Required if the event is an NDF (i.e. if IsNdf &#x3D; true).  Date of the FxRate fixings. | [optional] 
**settlement_ccy** | **str** | Optional.  Required if the event is an NDF (i.e. if IsNdf &#x3D; true).  May be set to either DomCcy or FgnCcy, or a third currency. | [optional] 
**cash_flow_per_unit** | **float** | Optional.  Required if the event is an NDF (i.e. if IsNdf &#x3D; true).  CashFlow per unit.  Paid in the SettlementCcy. | [optional] 
**domestic_to_foreign_rate** | **float** | Domestic currency to foreign currency FX rate.  Not required, only used to override quotes. | [optional] 
**domestic_to_settlement_rate** | **float** | Domestic currency to settlement currency FX rate  Not required, only used to override quotes. | [optional] 
**foreign_to_settlement_rate** | **float** | Foreign currency to settlement currency FX rate  Not required, only used to override quotes. | [optional] [readonly] 
**instrument_event_type** | **str** | The Type of Event. The available values are: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent, ExpiryEvent, ScripDividendEvent, StockDividendEvent, ReverseStockSplitEvent, CapitalDistributionEvent, SpinOffEvent, MergerEvent, FutureExpiryEvent, SwapCashFlowEvent, SwapPrincipalEvent, CreditPremiumCashFlowEvent, CdsCreditEvent, CdxCreditEvent, MbsCouponEvent, MbsPrincipalEvent, BonusIssueEvent, MbsPrincipalWriteOffEvent, MbsInterestDeferralEvent, MbsInterestShortfallEvent, TenderEvent, CallOnIntermediateSecuritiesEvent, IntermediateSecuritiesDistributionEvent, OptionExercisePhysicalEvent, OptionExerciseCashEvent, ProtectionPayoutCashFlowEvent, TermDepositInterestEvent, TermDepositPrincipalEvent, EarlyRedemptionEvent, FutureMarkToMarketEvent, AdjustGlobalCommitmentEvent, ContractInitialisationEvent, DrawdownEvent, LoanInterestRepaymentEvent, UpdateDepositAmountEvent, LoanPrincipalRepaymentEvent, DepositInterestPaymentEvent, DepositCloseEvent, LoanFacilityContractRolloverEvent, RepurchaseOfferEvent, RepoPartialClosureEvent, RepoCashFlowEvent, FlexibleRepoInterestPaymentEvent, FlexibleRepoCashFlowEvent, FlexibleRepoCollateralEvent, ConversionEvent, FlexibleRepoPartialClosureEvent, FlexibleRepoFullClosureEvent, CapletFloorletCashFlowEvent | 
## Example

```python
from lusid.models.fx_forward_settlement_event import FxForwardSettlementEvent
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

maturity_date: Optional[datetime] = # Replace with your value
dom_amount_per_unit: Union[StrictFloat, StrictInt] = # Replace with your value
dom_ccy: StrictStr = "example_dom_ccy"
fgn_amount_per_unit: Union[StrictFloat, StrictInt] = # Replace with your value
fgn_ccy: StrictStr = "example_fgn_ccy"
is_ndf: StrictBool = # Replace with your value
is_ndf:StrictBool = True
fixing_date: Optional[datetime] = # Replace with your value
settlement_ccy: Optional[StrictStr] = "example_settlement_ccy"
cash_flow_per_unit: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
domestic_to_foreign_rate: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
domestic_to_settlement_rate: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
foreign_to_settlement_rate: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
instrument_event_type: StrictStr = "example_instrument_event_type"
fx_forward_settlement_event_instance = FxForwardSettlementEvent(maturity_date=maturity_date, dom_amount_per_unit=dom_amount_per_unit, dom_ccy=dom_ccy, fgn_amount_per_unit=fgn_amount_per_unit, fgn_ccy=fgn_ccy, is_ndf=is_ndf, fixing_date=fixing_date, settlement_ccy=settlement_ccy, cash_flow_per_unit=cash_flow_per_unit, domestic_to_foreign_rate=domestic_to_foreign_rate, domestic_to_settlement_rate=domestic_to_settlement_rate, foreign_to_settlement_rate=foreign_to_settlement_rate, instrument_event_type=instrument_event_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

