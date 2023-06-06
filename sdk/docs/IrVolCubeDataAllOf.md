# IrVolCubeDataAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_date** | **datetime** | Base date of the cube - this is the start date of the swaptions on the cube. | 
**instruments** | [**List[LusidInstrument]**](LusidInstrument.md) | Retrieve the set of instruments that define the cube. | 
**quotes** | [**List[MarketQuote]**](MarketQuote.md) | Access the set of quotes that define the cube. | 
**lineage** | **str** | Description of the complex market data&#39;s lineage e.g. &#39;FundAccountant_GreenQuality&#39;. | [optional] 
**market_data_type** | **str** | The available values are: DiscountFactorCurveData, EquityVolSurfaceData, FxVolSurfaceData, IrVolCubeData, OpaqueMarketData, YieldCurveData, FxForwardCurveData, FxForwardPipsCurveData, FxForwardTenorCurveData, FxForwardTenorPipsCurveData, FxForwardCurveByQuoteReference, CreditSpreadCurveData, EquityCurveByPricesData | 

## Example

```python
from lusid.models.ir_vol_cube_data_all_of import IrVolCubeDataAllOf

# TODO update the JSON string below
json = "{}"
# create an instance of IrVolCubeDataAllOf from a JSON string
ir_vol_cube_data_all_of_instance = IrVolCubeDataAllOf.from_json(json)
# print the JSON string representation of the object
print IrVolCubeDataAllOf.to_json()

# convert the object into a dict
ir_vol_cube_data_all_of_dict = ir_vol_cube_data_all_of_instance.to_dict()
# create an instance of IrVolCubeDataAllOf from a dict
ir_vol_cube_data_all_of_form_dict = ir_vol_cube_data_all_of.from_dict(ir_vol_cube_data_all_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


