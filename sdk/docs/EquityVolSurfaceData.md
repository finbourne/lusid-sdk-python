# EquityVolSurfaceData

Market Data for an equity vol surface, represented by a list of instruments and corresponding market quotes

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_date** | **datetime** | Base date of the surface | 
**instruments** | [**list[LusidInstrument]**](LusidInstrument.md) | The set of instruments that define the surface. | 
**quotes** | [**list[MarketQuote]**](MarketQuote.md) | The set of market quotes that define the surface, in NormalVol or LogNormalVol terms. | 
**lineage** | **str** | Description of the complex market data&#39;s lineage e.g. &#39;FundAccountant_GreenQuality&#39;. | [optional] 
**market_data_type** | **str** | The available values are: DiscountFactorCurveData, EquityVolSurfaceData, FxVolSurfaceData, IrVolCubeData, OpaqueMarketData, YieldCurveData, FxForwardCurveData, FxForwardPipsCurveData, FxForwardTenorCurveData, FxForwardTenorPipsCurveData, FxForwardCurveByQuoteReference, CreditSpreadCurveData, EquityCurveByPricesData | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


