# FxSwap

LUSID representation of an FX Swap. Composed of two FX Forwards.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**near_fx_forward** | [**FxForward**](FxForward.md) |  | 
**far_fx_forward** | [**FxForward**](FxForward.md) |  | 
**notional_symmetry** | **str** | The NotionalSymmetry allows for even and uneven FxSwaps to be supported.  An even FxSwap is one where the near and far fx forwards have the same notional value on at least one of the  legs. An uneven FxSwap is one where near and far fx forwards don&#39;t have the same notional on both the  domestic and foreign legs.  By default NotionalSymmetry will be set as even.    Supported string (enumeration) values are: [Even, Uneven]. | [optional] 
**instrument_type** | **str** | The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond, InflationSwap | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


