# WholeLoanFacility

Whole Loan Facility. A loan facility wholly funded by a single lender: it shares the contractual terms, schedules  and instrument events of a LoanFacility, but ownership is not shared pro-rata across investors, and it is valued  at par rather than from a price quote. Like a LoanFacility, this is a lightweight instrument which acts as a  placeholder for the state that is built from the instrument events, with its contracts modelled via FlexibleLoan  instruments in LUSID.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **datetime** | The start date of the instrument. This is normally synonymous with the trade-date. | 
**maturity_date** | **datetime** | The final maturity date of the instrument. This means the last date on which the instruments makes a payment of any amount.  For the avoidance of doubt, that is not necessarily prior to its last sensitivity date for the purposes of risk; e.g. instruments such as  Constant Maturity Swaps (CMS) often have sensitivities to rates that may well be observed or set prior to the maturity date, but refer to a termination date beyond it. | 
**dom_ccy** | **str** | The domestic currency of the instrument. | 
**initial_commitment** | **float** | The initial commitment for the whole loan facility. | 
**loan_type** | **str** | LoanType for this facility. The facility can either be a revolving or a  term loan. Available values: Revolver, TermLoan. | 
**schedules** | [**List[Schedule]**](Schedule.md) | Repayment schedules for the facility. | 
**time_zone_conventions** | [**TimeZoneConventions**](TimeZoneConventions.md) |  | [optional] 
**instrument_type** | **str** | Available values: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap, SimpleCashFlowLoan, TotalReturnSwap, InflationLeg, FundShareClass, FlexibleLoan, UnsettledCash, Cash, MasteredInstrument, LoanFacility, FlexibleDeposit, FlexibleRepo, ToBeAnnounced, VolatilitySwap, ToBeAnnouncedOption, CommodityForward, BondOption, CdsOption, CommodityCalendarSwap, BondForward, PreferredShare, CapitalInterest, WholeLoanFacility. | 
## Example

```python
from lusid.models.whole_loan_facility import WholeLoanFacility
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

start_date: datetime = # Replace with your value
maturity_date: datetime = # Replace with your value
dom_ccy: StrictStr = "example_dom_ccy"
initial_commitment: Union[StrictFloat, StrictInt] = # Replace with your value
loan_type: StrictStr = "example_loan_type"
schedules: List[Schedule] = # Replace with your value
time_zone_conventions: Optional[TimeZoneConventions] = # Replace with your value
instrument_type: StrictStr = "example_instrument_type"
whole_loan_facility_instance = WholeLoanFacility(start_date=start_date, maturity_date=maturity_date, dom_ccy=dom_ccy, initial_commitment=initial_commitment, loan_type=loan_type, schedules=schedules, time_zone_conventions=time_zone_conventions, instrument_type=instrument_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

