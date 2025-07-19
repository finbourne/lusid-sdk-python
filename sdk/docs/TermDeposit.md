# TermDeposit

LUSID representation of a Term Deposit.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **datetime** | The start date of the instrument. For term deposits this is the start date of the interest calculation period. | 
**maturity_date** | **datetime** | The maturity date of the instrument. For term deposits this is the last date of the interest calculation period. | 
**contract_size** | **float** | The principal amount of the term deposit. | 
**flow_convention** | [**FlowConventions**](FlowConventions.md) |  | 
**rate** | **float** | The fixed rate for the term deposit. Specified as a decimal, e.g 0.03 is meant to be 3% interest | 
**dom_ccy** | **str** | The domestic currency of the instrument. This should be the same as the Currency set on the FlowConventions.  You do not need to populate this field for Term Deposits in LUSID as all functionality is driven by the Currency set on the FlowConventions.  LUSID will not store values saved on this field. | [optional] 
**trading_conventions** | [**TradingConventions**](TradingConventions.md) |  | [optional] 
**time_zone_conventions** | [**TimeZoneConventions**](TimeZoneConventions.md) |  | [optional] 
**instrument_type** | **str** | The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap, SimpleCashFlowLoan, TotalReturnSwap, InflationLeg, FundShareClass, FlexibleLoan, UnsettledCash, Cash, MasteredInstrument, LoanFacility, FlexibleDeposit, FlexibleRepo | 
## Example

```python
from lusid.models.term_deposit import TermDeposit
from typing import Any, Dict, Optional, Union
from pydantic.v1 import Field, StrictFloat, StrictInt, StrictStr, validator
from datetime import datetime
start_date: datetime = # Replace with your value
maturity_date: datetime = # Replace with your value
contract_size: Union[StrictFloat, StrictInt] = # Replace with your value
flow_convention: FlowConventions = # Replace with your value
rate: Union[StrictFloat, StrictInt] = # Replace with your value
dom_ccy: Optional[StrictStr] = "example_dom_ccy"
trading_conventions: Optional[TradingConventions] = # Replace with your value
time_zone_conventions: Optional[TimeZoneConventions] = # Replace with your value
instrument_type: StrictStr = "example_instrument_type"
term_deposit_instance = TermDeposit(start_date=start_date, maturity_date=maturity_date, contract_size=contract_size, flow_convention=flow_convention, rate=rate, dom_ccy=dom_ccy, trading_conventions=trading_conventions, time_zone_conventions=time_zone_conventions, instrument_type=instrument_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

