# ContractForDifferenceAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **datetime** | The start date of the CFD. | 
**maturity_date** | **datetime** | The maturity date for the CFD. If CFDType is Futures, this should be set to be the maturity date of the underlying  future. If CFDType is Cash, this should not be set. | [optional] 
**code** | **str** | The code of the underlying. | 
**contract_size** | **float** | The size of the CFD contract, this should represent the total number of stocks that the CFD represents. | 
**pay_ccy** | **str** | The currency that this CFD pays out, this can be different to the UnderlyingCcy. | 
**reference_rate** | **float** | The reference rate of the CFD, this can be set to 0 but not negative values.  This field is optional, if not set it will default to 0. | [optional] 
**type** | **str** | The type of CFD.    Supported string (enumeration) values are: [Cash, Futures]. | 
**underlying_ccy** | **str** | The currency of the underlying | 
**underlying_identifier** | **str** | external market codes and identifiers for the CFD, e.g. RIC.    Supported string (enumeration) values are: [LusidInstrumentId, Isin, Sedol, Cusip, ClientInternal, Figi, RIC, QuotePermId, REDCode, BBGId, ICECode]. | 
**instrument_type** | **str** | The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap, SimpleCashFlowLoan | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


