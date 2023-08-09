# TermDepositAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **datetime** | The start date of the instrument. For term deposits this is the start date of the interest calculation period. | 
**maturity_date** | **datetime** | The maturity date of the instrument. For term deposits this is the last date of the interest calculation period. | 
**contract_size** | **float** | The principal amount of the term deposit. | 
**flow_convention** | [**FlowConventions**](FlowConventions.md) |  | 
**rate** | **float** | The fixed rate for the term deposit. Specified as a decimal, e.g 0.03 is meant to be 3% interest | 
**dom_ccy** | **str** | The domestic currency of the instrument. This should be the same as the Currency set on the FlowConventions. | [optional] 
**instrument_type** | **str** | The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap, SimpleCashFlowLoan | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


