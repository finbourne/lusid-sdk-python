# IrVolDependency

Economic dependency required to price interest rate products that contain optionality, for example swaptions.  For example, can indicate a dependency on an IrVolCubeData.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency** | **str** | The domestic currency of the instrument declaring this dependency. | 
**vol_type** | **str** | Volatility type e.g. \&quot;LN\&quot; and \&quot;N\&quot; for log-normal and normal volatility. | 
**var_date** | **datetime** | The effectiveDate of the entity that this is a dependency for.  Unless there is an obvious date this should be, like for a historic reset, then this is the valuation date. | 
**dependency_type** | **str** | The available values are: OpaqueDependency, CashDependency, DiscountingDependency, EquityCurveDependency, EquityVolDependency, FxDependency, FxForwardsDependency, FxVolDependency, IndexProjectionDependency, IrVolDependency, QuoteDependency, Vendor, CalendarDependency, InflationFixingDependency | 

## Example

```python
from lusid.models.ir_vol_dependency import IrVolDependency

# TODO update the JSON string below
json = "{}"
# create an instance of IrVolDependency from a JSON string
ir_vol_dependency_instance = IrVolDependency.from_json(json)
# print the JSON string representation of the object
print IrVolDependency.to_json()

# convert the object into a dict
ir_vol_dependency_dict = ir_vol_dependency_instance.to_dict()
# create an instance of IrVolDependency from a dict
ir_vol_dependency_form_dict = ir_vol_dependency.from_dict(ir_vol_dependency_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


