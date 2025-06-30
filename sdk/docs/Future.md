# Future

LUSID representation of a Future.  Including, but not limited to, Equity Futures, Bond Futures, Index Futures, Currency Futures, and Interest Rate Futures.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **datetime** | The start date of the instrument. This is normally synonymous with the trade-date. | 
**maturity_date** | **datetime** | The final maturity date of the instrument. This means the last date on which the instruments makes a payment of any amount.  For the avoidance of doubt, that is not necessarily prior to its last sensitivity date for the purposes of risk; e.g. instruments such as  Constant Maturity Swaps (CMS) often have sensitivities to rates that may well be observed or set prior to the maturity date, but refer to a termination date beyond it. | 
**identifiers** | **Dict[str, str]** | External market codes and identifiers for the bond, e.g. ISIN. | 
**contract_details** | [**FuturesContractDetails**](FuturesContractDetails.md) |  | 
**contracts** | **float** | The number of contracts held. This is optional and will default to 1 if not set.  Instrument events will only work when this field is 1.  We recommend not using this field and instead relying on the number of holdings to   represent the number of futures contracts. | [optional] [default to 1]
**mark_to_market_conventions** | [**MarkToMarketConventions**](MarkToMarketConventions.md) |  | [optional] 
**ref_spot_price** | **float** | The reference spot price for the future at which the contract was entered into. | [optional] 
**underlying** | [**LusidInstrument**](LusidInstrument.md) |  | [optional] 
**calculation_type** | **str** | Calculation type for some Future instruments which have non-standard methodology.  Optional, if not set defaults as follows:  - If ExchangeCode is \&quot;ASX\&quot; and ContractCode is \&quot;IR\&quot; or \&quot;BB\&quot; set to ASX_BankBills  - If ExchangeCode is \&quot;ASX\&quot; and ContractCode is \&quot;YT\&quot; set to ASX_3Year  - If ExchangeCode is \&quot;ASX\&quot; and ContractCode is \&quot;VT\&quot; set to ASX_5Year  - If ExchangeCode is \&quot;ASX\&quot; and ContractCode is \&quot;XT\&quot; set to ASX_10Year  - If ExchangeCode is \&quot;ASX\&quot; and ContractCode is \&quot;LT\&quot; set to ASX_20Year  - otherwise set to Standard                Specific calculation types for bond and interest rate futures are:  - [Standard] The default calculation type, which does not fit into any of the categories below.  - [ASX_BankBills] Used for AUD and NZD futures “IR” and “BB” on ASX. 90D Bank Bills.  - [ASX_3Year] Used for “YT” on ASX. 3YR semi-annual bond (6 coupons) @ 6%.  - [ASX_5Year] Used for “VT” on ASX. 5yr semi-annual bond (10 coupons) @ 2%.  - [ASX_10Year] Used for “XT” on ASX. 10yr semi-annual bond (20 coupons) @ 6%.  - [ASX_20Year] Used for “LT” on ASX. 20yr semi-annual bond (40 coupons) @ 4%.  - [B3_DI1] Used for “DI1” on B3. Average of 1D interbank deposit rates.    - For futures with this calculation type, quote values are expected to be specified as a percentage.      For example, a quoted rate of 13.205% should be specified as a quote of 13.205 with a face value of 100.                Supported string (enumeration) values are: [Standard, ASX_BankBills, ASX_3Year, ASX_5Year, ASX_10Year, ASX_20Year, B3_DI1]. | [optional] 
**trading_conventions** | [**TradingConventions**](TradingConventions.md) |  | [optional] 
**instrument_type** | **str** | The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap, SimpleCashFlowLoan, TotalReturnSwap, InflationLeg, FundShareClass, FlexibleLoan, UnsettledCash, Cash, MasteredInstrument, LoanFacility, FlexibleDeposit | 
## Example

```python
from lusid.models.future import Future
from typing import Any, Dict, Optional, Union
from pydantic.v1 import Field, StrictFloat, StrictInt, StrictStr, constr, validator
from datetime import datetime
start_date: datetime = # Replace with your value
maturity_date: datetime = # Replace with your value
identifiers: Dict[str, StrictStr] = # Replace with your value
contract_details: FuturesContractDetails = # Replace with your value
contracts: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
mark_to_market_conventions: Optional[MarkToMarketConventions] = # Replace with your value
ref_spot_price: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
underlying: Optional[LusidInstrument] = None
calculation_type: Optional[StrictStr] = "example_calculation_type"
trading_conventions: Optional[TradingConventions] = # Replace with your value
instrument_type: StrictStr = "example_instrument_type"
future_instance = Future(start_date=start_date, maturity_date=maturity_date, identifiers=identifiers, contract_details=contract_details, contracts=contracts, mark_to_market_conventions=mark_to_market_conventions, ref_spot_price=ref_spot_price, underlying=underlying, calculation_type=calculation_type, trading_conventions=trading_conventions, instrument_type=instrument_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

