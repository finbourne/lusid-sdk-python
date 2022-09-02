# SimpleInstrument

LUSID representation of a Simple Instrument, used as a basic definition of a generic instrument.  No analytics can be obtained for this.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**maturity_date** | **datetime** | The final maturity date of the instrument. This means the last date on which the instruments makes a payment of any amount.  For the avoidance of doubt, that is not necessarily prior to its last sensitivity date for the purposes of risk; e.g. instruments such as  Constant Maturity Swaps (CMS) often have sensitivities to rates that may well be observed or set prior to the maturity date, but refer to a termination date beyond it. | [optional] 
**dom_ccy** | **str** | The domestic currency. | 
**asset_class** | **str** | The available values are: InterestRates, FX, Inflation, Equities, Credit, Commodities, Money, Unknown | 
**fgn_ccys** | **list[str]** | The set of foreign currencies, if any (optional). | [optional] 
**simple_instrument_type** | **str** | The Instrument type of the simple instrument. | 
**instrument_type** | **str** | The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

