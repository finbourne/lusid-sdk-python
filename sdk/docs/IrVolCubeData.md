# IrVolCubeData

Market Data required to build a volatility cube for swaption pricing,  represented by a list of instruments and corresponding market quotes

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_date** | **datetime** | Base date of the cube - this is the start date of the swaptions on the cube. | 
**instruments** | [**List[LusidInstrument]**](LusidInstrument.md) | Retrieve the set of instruments that define the cube. | 
**quotes** | [**List[MarketQuote]**](MarketQuote.md) | Access the set of quotes that define the cube. | 
**lineage** | **str** | Description of the complex market data&#39;s lineage e.g. &#39;FundAccountant_GreenQuality&#39;. | [optional] 
**market_data_type** | **str** | The available values are: DiscountFactorCurveData, EquityVolSurfaceData, FxVolSurfaceData, IrVolCubeData, OpaqueMarketData, YieldCurveData, FxForwardCurveData, FxForwardPipsCurveData, FxForwardTenorCurveData, FxForwardTenorPipsCurveData, FxForwardCurveByQuoteReference, CreditSpreadCurveData, EquityCurveByPricesData, ConstantVolatilitySurface | 

## Example

```python
from lusid.models.ir_vol_cube_data import IrVolCubeData

# TODO update the JSON string below
json = "{}"
# create an instance of IrVolCubeData from a JSON string
ir_vol_cube_data_instance = IrVolCubeData.from_json(json)
# print the JSON string representation of the object
print IrVolCubeData.to_json()

# convert the object into a dict
ir_vol_cube_data_dict = ir_vol_cube_data_instance.to_dict()
# create an instance of IrVolCubeData from a dict
ir_vol_cube_data_form_dict = ir_vol_cube_data.from_dict(ir_vol_cube_data_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


