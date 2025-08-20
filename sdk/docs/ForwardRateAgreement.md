# ForwardRateAgreement

LUSID representation of a Forward Rate Agreement.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **datetime** | The settlement date of the FRA | 
**maturity_date** | **datetime** | The final maturity date of the instrument. This means the last date on which the instruments makes a payment of any amount. For the avoidance of doubt, that is not necessarily prior to its last sensitivity date for the purposes of risk; e.g. instruments such as Constant Maturity Swaps (CMS) often have sensitivities to rates beyond their last payment date. | 
**dom_ccy** | **str** | The domestic currency of the instrument. | 
**fixing_date** | **datetime** | The date at which the rate to be paid, the reference rate, is confirmed/observed. | 
**fra_rate** | **float** | The rate at which the FRA is traded. | 
**notional** | **float** | The amount for which the FRA is traded. | 
**index_convention** | [**IndexConvention**](IndexConvention.md) |  | [optional] 
**time_zone_conventions** | [**TimeZoneConventions**](TimeZoneConventions.md) |  | [optional] 
**instrument_type** | **str** | The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap, SimpleCashFlowLoan, TotalReturnSwap, InflationLeg, FundShareClass, FlexibleLoan, UnsettledCash, Cash, MasteredInstrument, LoanFacility, FlexibleDeposit, FlexibleRepo | 
## Example

```python
from lusid.models.forward_rate_agreement import ForwardRateAgreement
from typing import Any, Dict, Optional, Union
from pydantic.v1 import Field, StrictFloat, StrictInt, StrictStr, validator
from datetime import datetime
start_date: datetime = # Replace with your value
maturity_date: datetime = # Replace with your value
dom_ccy: StrictStr = "example_dom_ccy"
fixing_date: datetime = # Replace with your value
fra_rate: Union[StrictFloat, StrictInt] = # Replace with your value
notional: Union[StrictFloat, StrictInt] = # Replace with your value
index_convention: Optional[IndexConvention] = # Replace with your value
time_zone_conventions: Optional[TimeZoneConventions] = # Replace with your value
instrument_type: StrictStr = "example_instrument_type"
forward_rate_agreement_instance = ForwardRateAgreement(start_date=start_date, maturity_date=maturity_date, dom_ccy=dom_ccy, fixing_date=fixing_date, fra_rate=fra_rate, notional=notional, index_convention=index_convention, time_zone_conventions=time_zone_conventions, instrument_type=instrument_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

