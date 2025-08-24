# ExchangeTradedOption

LUSID representation of an Exchange Traded Option.  Including, but not limited to, Equity Options, Bond Options, Index Options, Future Options, and Interest Rate Options.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **datetime** | The start date of the instrument. This is normally synonymous with the trade-date. | 
**contract_details** | [**ExchangeTradedOptionContractDetails**](ExchangeTradedOptionContractDetails.md) |  | 
**contracts** | **float** | The number of contracts held. | 
**ref_spot_price** | **float** | The reference spot price for the option at which the contract was entered into. | 
**trading_conventions** | [**TradingConventions**](TradingConventions.md) |  | [optional] 
**time_zone_conventions** | [**TimeZoneConventions**](TimeZoneConventions.md) |  | [optional] 
**instrument_type** | **str** | The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap, SimpleCashFlowLoan, TotalReturnSwap, InflationLeg, FundShareClass, FlexibleLoan, UnsettledCash, Cash, MasteredInstrument, LoanFacility, FlexibleDeposit, FlexibleRepo | 
## Example

```python
from lusid.models.exchange_traded_option import ExchangeTradedOption
from typing import Any, Dict, Optional, Union
from pydantic.v1 import Field, StrictFloat, StrictInt, StrictStr, validator
from datetime import datetime
start_date: datetime = # Replace with your value
contract_details: ExchangeTradedOptionContractDetails = # Replace with your value
contracts: Union[StrictFloat, StrictInt] = # Replace with your value
ref_spot_price: Union[StrictFloat, StrictInt] = # Replace with your value
trading_conventions: Optional[TradingConventions] = # Replace with your value
time_zone_conventions: Optional[TimeZoneConventions] = # Replace with your value
instrument_type: StrictStr = "example_instrument_type"
exchange_traded_option_instance = ExchangeTradedOption(start_date=start_date, contract_details=contract_details, contracts=contracts, ref_spot_price=ref_spot_price, trading_conventions=trading_conventions, time_zone_conventions=time_zone_conventions, instrument_type=instrument_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

