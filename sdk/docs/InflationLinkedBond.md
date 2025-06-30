# InflationLinkedBond

Inflation Linked Bond.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **datetime** | The start date of the bond. | 
**maturity_date** | **datetime** | The final maturity date of the instrument. This means the last date on which the instruments makes a payment of any amount.  For the avoidance of doubt, that is not necessarily prior to its last sensitivity date for the purposes of risk; e.g. instruments such as  Constant Maturity Swaps (CMS) often have sensitivities to rates that may well be observed or set prior to the maturity date, but refer to a termination date beyond it. | 
**flow_conventions** | [**FlowConventions**](FlowConventions.md) |  | 
**inflation_index_conventions** | [**InflationIndexConventions**](InflationIndexConventions.md) |  | 
**coupon_rate** | **float** | Simple coupon rate. | 
**identifiers** | **Dict[str, str]** | External market codes and identifiers for the bond, e.g. ISIN. | [optional] 
**base_cpi** | **float** | BaseCPI value. This is optional, if not provided the BaseCPI value will be calculated from the BaseCPIDate,  if that too is not present the StartDate will be used.                If provided then this value will always set the BaseCPI on this bond.                The BaseCPI of an inflation linked bond is calculated using the following logic:  - If a BaseCPI value is provided, this is used.  - Otherwise, if BaseCPIDate is provided, the CPI for this date is calculated and used.  - Otherwise, the CPI for the StartDate is calculated and used.                Note that if both BaseCPI and BaseCPIDate are set, the BaseCPI value will be used and the BaseCPIDate  will be ignored but can still be added for informative purposes.                Some bonds are issued with a BaseCPI date that does not correspond to the StartDate CPI value, in this  case the value should be provided here or with the BaseCPIDate. | [optional] 
**base_cpi_date** | **datetime** | BaseCPIDate. This is optional. Gives the date that the BaseCPI is calculated for.                Note this is an un-lagged date (similar to StartDate) so the Bond ObservationLag will  be applied to this date when calculating the CPI.                The BaseCPI of an inflation linked bond is calculated using the following logic:  - If a BaseCPI value is provided, this is used.  - Otherwise, if BaseCPIDate is provided, the CPI for this date is calculated and used.  - Otherwise, the CPI for the StartDate is calculated and used.                Note that if both BaseCPI and BaseCPIDate are set, the BaseCPI value will be used and the BaseCPIDate  will be ignored but can still be added for informative purposes.                Some bonds are issued with a BaseCPI date that does not correspond to the StartDate CPI value, in this  case the value should be provided here or with the actual BaseCPI. | [optional] 
**calculation_type** | **str** | The calculation type applied to the bond coupon and principal amount.  The default CalculationType is &#x60;Standard&#x60;.    Supported string (enumeration) values are: [Standard, Quarterly, Ratio, Brazil, StandardAccruedOnly, RatioAccruedOnly, StandardWithCappedAccruedInterest]. | [optional] 
**ex_dividend_days** | **int** | Number of Good Business Days before the next coupon payment, in which the bond goes ex-dividend. | [optional] 
**index_precision** | **int** | Number of decimal places used to round IndexRatio. This defaults to 5 if not set. | [optional] 
**principal** | **float** | The face-value or principal for the bond at outset. | 
**principal_protection** | **bool** | If true then the principal is protected in that the redemption amount will be at least the face value (Principal).  This is typically set to true for inflation linked bonds issued by the United States and France (for example).  This is typically set to false for inflation linked bonds issued by the United Kingdom (post 2005).  For other sovereigns this can vary from issue to issue.  If not set this property defaults to true.  This is sometimes referred to as Deflation protection or an inflation floor of 0%. | [optional] 
**stub_type** | **str** | StubType. Most Inflation linked bonds have a ShortFront stub type so this is the default, however in some cases  with a long front stub LongFront should be selected.  StubType Both is not supported for InflationLinkedBonds.    Supported string (enumeration) values are: [ShortFront, ShortBack, LongBack, LongFront, Both]. | [optional] 
**rounding_conventions** | [**List[RoundingConvention]**](RoundingConvention.md) | Rounding conventions for analytics, if any. | [optional] 
**trading_conventions** | [**TradingConventions**](TradingConventions.md) |  | [optional] 
**original_issue_price** | **float** | The price the bond was issued at. This is to be entered as a percentage of par, for example a value of 98.5 would represent 98.5%. | [optional] 
**instrument_type** | **str** | The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap, SimpleCashFlowLoan, TotalReturnSwap, InflationLeg, FundShareClass, FlexibleLoan, UnsettledCash, Cash, MasteredInstrument, LoanFacility, FlexibleDeposit | 
## Example

```python
from lusid.models.inflation_linked_bond import InflationLinkedBond
from typing import Any, Dict, List, Optional, Union
from pydantic.v1 import Field, StrictBool, StrictFloat, StrictInt, StrictStr, conlist, constr, validator
from datetime import datetime
start_date: datetime = # Replace with your value
maturity_date: datetime = # Replace with your value
flow_conventions: FlowConventions = # Replace with your value
inflation_index_conventions: InflationIndexConventions = # Replace with your value
coupon_rate: Union[StrictFloat, StrictInt] = # Replace with your value
identifiers: Optional[Dict[str, StrictStr]] = # Replace with your value
base_cpi: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
base_cpi_date: Optional[datetime] = # Replace with your value
calculation_type: Optional[StrictStr] = "example_calculation_type"
ex_dividend_days: Optional[StrictInt] = # Replace with your value
ex_dividend_days: Optional[StrictInt] = None
index_precision: Optional[StrictInt] = # Replace with your value
index_precision: Optional[StrictInt] = None
principal: Union[StrictFloat, StrictInt] = # Replace with your value
principal_protection: Optional[StrictBool] = # Replace with your value
principal_protection:Optional[StrictBool] = None
stub_type: Optional[StrictStr] = "example_stub_type"
rounding_conventions: Optional[conlist(RoundingConvention)] = # Replace with your value
trading_conventions: Optional[TradingConventions] = # Replace with your value
original_issue_price: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
instrument_type: StrictStr = "example_instrument_type"
inflation_linked_bond_instance = InflationLinkedBond(start_date=start_date, maturity_date=maturity_date, flow_conventions=flow_conventions, inflation_index_conventions=inflation_index_conventions, coupon_rate=coupon_rate, identifiers=identifiers, base_cpi=base_cpi, base_cpi_date=base_cpi_date, calculation_type=calculation_type, ex_dividend_days=ex_dividend_days, index_precision=index_precision, principal=principal, principal_protection=principal_protection, stub_type=stub_type, rounding_conventions=rounding_conventions, trading_conventions=trading_conventions, original_issue_price=original_issue_price, instrument_type=instrument_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

