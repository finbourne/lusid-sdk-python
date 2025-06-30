# LoanFacility

Loan Facility. This is a very lightweight instrument which acts as a placeholder for the state that is built  from the instrument events. The facility acts as an agreement between a single borrower and many lenders (investors).  Several contracts may be drawn up to enable the lending of funds to the borrower. These contracts are modelled via  FlexibleLoan instruments in LUSID. The instrument events on the facility may relate to the facility as a whole  (for example to define a global commitment amount), or they may relate to a single contract (such as a paydown  transaction on a particular contract).
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **datetime** | The start date of the instrument. This is normally synonymous with the trade-date. | 
**maturity_date** | **datetime** | The final maturity date of the instrument. This means the last date on which the instruments makes a payment of any amount.  For the avoidance of doubt, that is not necessarily prior to its last sensitivity date for the purposes of risk; e.g. instruments such as  Constant Maturity Swaps (CMS) often have sensitivities to rates that may well be observed or set prior to the maturity date, but refer to a termination date beyond it. | 
**dom_ccy** | **str** | The domestic currency of the instrument. | 
**initial_commitment** | **float** | The initial commitment for the loan facility. | 
**loan_type** | **str** | LoanType for this facility. The facility can either be a revolving or a  term loan.    Supported string (enumeration) values are: [Revolver, TermLoan]. | 
**schedules** | [**List[Schedule]**](Schedule.md) | Repayment schedules for the loan. | 
**instrument_type** | **str** | The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap, SimpleCashFlowLoan, TotalReturnSwap, InflationLeg, FundShareClass, FlexibleLoan, UnsettledCash, Cash, MasteredInstrument, LoanFacility, FlexibleDeposit | 
## Example

```python
from lusid.models.loan_facility import LoanFacility
from typing import Any, Dict, List, Union
from pydantic.v1 import Field, StrictFloat, StrictInt, StrictStr, conlist, constr, validator
from datetime import datetime
start_date: datetime = # Replace with your value
maturity_date: datetime = # Replace with your value
dom_ccy: StrictStr = "example_dom_ccy"
initial_commitment: Union[StrictFloat, StrictInt] = # Replace with your value
loan_type: StrictStr = "example_loan_type"
schedules: conlist(Schedule) = # Replace with your value
instrument_type: StrictStr = "example_instrument_type"
loan_facility_instance = LoanFacility(start_date=start_date, maturity_date=maturity_date, dom_ccy=dom_ccy, initial_commitment=initial_commitment, loan_type=loan_type, schedules=schedules, instrument_type=instrument_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

