# ContractForDifference

LUSID representation of a Contract for Difference.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **datetime** | The start date of the CFD. | 
**maturity_date** | **datetime** | The maturity date for the CFD. If CFDType is Futures, this should be set to be the maturity date of the underlying  future. If CFDType is Cash, this should not be set. | [optional] 
**code** | **str** | The code of the underlying. | [optional] 
**contract_size** | **float** | The size of the CFD contract, this should represent the total number of stocks that the CFD represents.   This field is optional, if not set it will default to 1. | [optional] 
**pay_ccy** | **str** | The currency that this CFD pays out, this can be different to the UnderlyingCcy. | 
**reference_rate** | **float** | The reference rate of the CFD, this can be set to 0 but not negative values.  This field is optional, if not set it will default to 0. | [optional] 
**type** | **str** | The type of CFD.    Supported string (enumeration) values are: [Cash, Futures]. | 
**underlying_ccy** | **str** | The currency of the underlying | [optional] 
**underlying_identifier** | **str** | External market codes and identifiers for the CFD, e.g. RIC.    Supported string (enumeration) values are: [LusidInstrumentId, Isin, Sedol, Cusip, ClientInternal, Figi, RIC, QuotePermId, REDCode, BBGId, ICECode]. | [optional] 
**lot_size** | **int** | CFD LotSize, the minimum number of shares that can be bought or sold at once.  Optional, if set must be non-negative, if not set defaults to 1. | [optional] 
**underlying** | [**LusidInstrument**](LusidInstrument.md) |  | [optional] 
**instrument_type** | **str** | The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap, SimpleCashFlowLoan, TotalReturnSwap, InflationLeg, FundShareClass, FlexibleLoan, UnsettledCash, Cash, MasteredInstrument, LoanFacility, FlexibleDeposit | 
## Example

```python
from lusid.models.contract_for_difference import ContractForDifference
from typing import Any, Dict, Optional, Union
from pydantic.v1 import Field, StrictFloat, StrictInt, StrictStr, constr, validator
from datetime import datetime
start_date: datetime = # Replace with your value
maturity_date: Optional[datetime] = # Replace with your value
code: Optional[StrictStr] = "example_code"
contract_size: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
pay_ccy: StrictStr = "example_pay_ccy"
reference_rate: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
type: StrictStr = "example_type"
underlying_ccy: Optional[StrictStr] = "example_underlying_ccy"
underlying_identifier: Optional[StrictStr] = "example_underlying_identifier"
lot_size: Optional[StrictInt] = # Replace with your value
lot_size: Optional[StrictInt] = None
underlying: Optional[LusidInstrument] = None
instrument_type: StrictStr = "example_instrument_type"
contract_for_difference_instance = ContractForDifference(start_date=start_date, maturity_date=maturity_date, code=code, contract_size=contract_size, pay_ccy=pay_ccy, reference_rate=reference_rate, type=type, underlying_ccy=underlying_ccy, underlying_identifier=underlying_identifier, lot_size=lot_size, underlying=underlying, instrument_type=instrument_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

