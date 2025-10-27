# FxForward

LUSID representation of an FX Forward.  Including FX Spot and Non-Deliverable Forwards.                This instrument has multiple legs, to see how legs are used in LUSID see [knowledge base article KA-02252](https://support.lusid.com/knowledgebase/article/KA-02252).                | Leg Index | Leg Identifier | Description |  | --------- | -------------- | ----------- |  | 1 | DomesticLeg | Cash flows in the domestic currency of the forward. |  | 2 | ForeignLeg | Cash flows in the foreign currency of the forward (not present for non-deliverable forwards). |
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **datetime** | The start date of the instrument. This is normally synonymous with the trade-date. | 
**maturity_date** | **datetime** | The final maturity date of the instrument. This means the last date on which the instruments makes a payment of any amount.  For the avoidance of doubt, that is not necessarily prior to its last sensitivity date for the purposes of risk; e.g. instruments such as  Constant Maturity Swaps (CMS) often have sensitivities to rates that may well be observed or set prior to the maturity date, but refer to a termination date beyond it. | 
**dom_amount** | **float** | The amount that is to be paid in the domestic currency on the maturity date. | 
**dom_ccy** | **str** | The domestic currency of the instrument. | 
**fgn_amount** | **float** | The amount that is to be paid in the foreign currency on the maturity date. | 
**fgn_ccy** | **str** | The foreign (other) currency of the instrument. In the NDF case, only payments are made in the domestic currency.  For the outright forward, currencies are exchanged. | 
**ref_spot_rate** | **float** | The reference Fx Spot rate for currency pair Foreign-Domestic that was seen on the trade start date (time). | [optional] 
**is_ndf** | **bool** | Is the contract an Fx-Forward of \&quot;Non-Deliverable\&quot; type, meaning a single payment in the domestic currency based on the change in fx-rate vs  a reference rate is used.  Defaults to false if not set. | [optional] 
**fixing_date** | **datetime** | The fixing date. | [optional] 
**settlement_ccy** | **str** | The settlement currency.  If provided, present value will be calculated in settlement currency, otherwise the domestic currency. Applies only to non-deliverable FX Forwards. | [optional] 
**booked_as_spot** | **bool** | Boolean flag for FX Forward transactions booked with Spot settlement. This will default to False if not provided.  For information purposes only, this does not impact LUSID valuation, analytics, cashflows or events, but may be used by third party vendors. | [optional] 
**time_zone_conventions** | [**TimeZoneConventions**](TimeZoneConventions.md) |  | [optional] 
**instrument_type** | **str** | The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap, SimpleCashFlowLoan, TotalReturnSwap, InflationLeg, FundShareClass, FlexibleLoan, UnsettledCash, Cash, MasteredInstrument, LoanFacility, FlexibleDeposit, FlexibleRepo | 
## Example

```python
from lusid.models.fx_forward import FxForward
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

start_date: datetime = # Replace with your value
maturity_date: datetime = # Replace with your value
dom_amount: Union[StrictFloat, StrictInt] = # Replace with your value
dom_ccy: StrictStr = "example_dom_ccy"
fgn_amount: Union[StrictFloat, StrictInt] = # Replace with your value
fgn_ccy: StrictStr = "example_fgn_ccy"
ref_spot_rate: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
is_ndf: Optional[StrictBool] = # Replace with your value
is_ndf:Optional[StrictBool] = None
fixing_date: Optional[datetime] = # Replace with your value
settlement_ccy: Optional[StrictStr] = "example_settlement_ccy"
booked_as_spot: Optional[StrictBool] = # Replace with your value
booked_as_spot:Optional[StrictBool] = None
time_zone_conventions: Optional[TimeZoneConventions] = # Replace with your value
instrument_type: StrictStr = "example_instrument_type"
fx_forward_instance = FxForward(start_date=start_date, maturity_date=maturity_date, dom_amount=dom_amount, dom_ccy=dom_ccy, fgn_amount=fgn_amount, fgn_ccy=fgn_ccy, ref_spot_rate=ref_spot_rate, is_ndf=is_ndf, fixing_date=fixing_date, settlement_ccy=settlement_ccy, booked_as_spot=booked_as_spot, time_zone_conventions=time_zone_conventions, instrument_type=instrument_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

