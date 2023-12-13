# ConstantVolatilitySurface

Market Data required to build a volatility surface for pricing.  Single constant volatility point.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_date** | **datetime** | Base date of the engine - this is the reference date for resolution of tenors. | 
**asset_type** | **str** | What is the asset that the engine is for.  Supported string (enumeration) values are: [Cash, Commodity, Credit, Equity, Fx, Rates, FxVol, IrVol, EquityVol, HolidayCalendar, IndexConvention, FlowConvention, CdsFlowConvention, CorporateActions, FxForwards, Quote, Inflation, EquityCurve, All, VendorOpaque]. | 
**lineage** | **str** |  | [optional] 
**volatility** | **float** | Volatility value. | 
**market_data_type** | **str** | The available values are: DiscountFactorCurveData, EquityVolSurfaceData, FxVolSurfaceData, IrVolCubeData, OpaqueMarketData, YieldCurveData, FxForwardCurveData, FxForwardPipsCurveData, FxForwardTenorCurveData, FxForwardTenorPipsCurveData, FxForwardCurveByQuoteReference, CreditSpreadCurveData, EquityCurveByPricesData, ConstantVolatilitySurface | 

## Example

```python
from lusid.models.constant_volatility_surface import ConstantVolatilitySurface

# TODO update the JSON string below
json = "{}"
# create an instance of ConstantVolatilitySurface from a JSON string
constant_volatility_surface_instance = ConstantVolatilitySurface.from_json(json)
# print the JSON string representation of the object
print ConstantVolatilitySurface.to_json()

# convert the object into a dict
constant_volatility_surface_dict = constant_volatility_surface_instance.to_dict()
# create an instance of ConstantVolatilitySurface from a dict
constant_volatility_surface_form_dict = constant_volatility_surface.from_dict(constant_volatility_surface_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


