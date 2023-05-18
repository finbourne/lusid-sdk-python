# InflationSwapAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **datetime** | The start date of the instrument. This is normally synonymous with the trade-date. | 
**maturity_date** | **datetime** | The final maturity date of the instrument. This means the last date on which the instruments makes a payment of any amount.  For the avoidance of doubt, that is not necessarily prior to its last sensitivity date for the purposes of risk; e.g. instruments such as  Constant Maturity Swaps (CMS) often have sensitivities to rates that may well be observed or set prior to the maturity date, but refer to a termination date beyond it. | 
**flow_conventions** | [**FlowConventions**](FlowConventions.md) |  | 
**fixed_rate** | **float** | Fixed Rate | 
**inflation_cap** | **float** | Optional cap, needed for LPI swaps. Should not be set for ZCIIS. | [optional] 
**inflation_floor** | **float** | Optional floor, needed for LPI swaps. Should not be set for ZCIIS. | [optional] 
**inflation_frequency** | **str** | Frequency of inflation updated. Optional and defaults to Monthly which is the most common.  However both Australian and New Zealand inflation is published Quarterly. Only tenors of 1M or 3M are supported. | [optional] 
**inflation_index_name** | **str** | Name of the Inflation Index | 
**inflation_interpolation** | **str** | Inflation Interpolation flag, defaults to Linear but some older swaps require Flat.    Supported string (enumeration) values are: [Linear, Flat]. | [optional] 
**inflation_roll_day** | **int** | Day of the month that inflation rolls from one month to the next. This is optional and defaults to 1, which is  the typically value for the majority of inflation bonds (exceptions include Japan which rolls on the 10th  and some LatAm bonds which roll on the 15th). | [optional] 
**notional** | **float** | The notional | 
**observation_lag** | **str** | Observation Lag, must be a number of Months, typically 3 or 4 but sometimes 8. | 
**pay_receive** | **str** | PayReceive flag for the inflation leg.  This field is optional and defaults to Pay.  If set to Pay, this swap pays inflation and receives fixed.    Supported string (enumeration) values are: [Pay, Receive]. | [optional] 
**instrument_type** | **str** | The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap, SimpleCashFlowLoan | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


