# IrVolCubeData

Market Data required to build a volatility cube for swaption pricing,  represented by a list of instruments and corresponding market quotes

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_date** | **datetime** | Base date of the cube - this is the start date of the swaptions on the cube. | 
**instruments** | [**list[LusidInstrument]**](LusidInstrument.md) | Retrieve the set of instruments that define the cube. | 
**quotes** | [**list[MarketQuote]**](MarketQuote.md) | Access the set of quotes that define the cube. | 
**lineage** | **str** | Description of the complex market data&#39;s lineage e.g. &#39;FundAccountant_GreenQuality&#39;. | [optional] 
**market_data_type** | **str** | The available values are: DiscountFactorCurveData, EquityVolSurfaceData, FxVolSurfaceData, IrVolCubeData, OpaqueMarketData, YieldCurveData, FxForwardCurveData, FxForwardPipsCurveData, FxForwardTenorCurveData, FxForwardTenorPipsCurveData, FxForwardCurveByQuoteReference, CreditSpreadCurveData, EquityCurveByPricesData | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


