# CreditSpreadCurveDataAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_date** | **datetime** | EffectiveAt date of the quoted rates | 
**dom_ccy** | **str** | Domestic currency of the curve | 
**tenors** | **list[str]** | The tenors for which the rates apply | 
**spreads** | **list[float]** | Par spread quotes corresponding to the tenors. | 
**recovery_rate** | **float** | The recovery rate in default. | 
**reference_date** | **datetime** | If tenors are provided, this is the date against which the tenors will be resolved.  This is of importance to CDX spread quotes, which are usually quoted in tenors relative to the CDX start date.  In this case, the ReferenceDate would be equal to the CDX start date, and the BaseDate would be the date for which the spreads are valid.  If not provided, this defaults to the BaseDate of the curve. | [optional] 
**maturities** | **list[datetime]** | The maturity dates for which the rates apply.  Either tenors or maturities should be provided, not both. | [optional] 
**lineage** | **str** | Description of the complex market data&#39;s lineage e.g. &#39;FundAccountant_GreenQuality&#39;. | [optional] 
**market_data_type** | **str** | The available values are: DiscountFactorCurveData, EquityVolSurfaceData, FxVolSurfaceData, IrVolCubeData, OpaqueMarketData, YieldCurveData, FxForwardCurveData, FxForwardPipsCurveData, FxForwardTenorCurveData, FxForwardTenorPipsCurveData, FxForwardCurveByQuoteReference, CreditSpreadCurveData, EquityCurveByPricesData | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


