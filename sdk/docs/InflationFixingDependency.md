# InflationFixingDependency

For indicating a dependency upon an inflation fixing

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The Type of fixing (index, ratio or assumption) | 
**code** | **str** | The Code of the fixing, typically the index name | 
**var_date** | **datetime** | The effectiveAt of the inflation fixing | 
**dependency_type** | **str** | The available values are: OpaqueDependency, CashDependency, DiscountingDependency, EquityCurveDependency, EquityVolDependency, FxDependency, FxForwardsDependency, FxVolDependency, IndexProjectionDependency, IrVolDependency, QuoteDependency, Vendor, CalendarDependency, InflationFixingDependency | 

## Example

```python
from lusid.models.inflation_fixing_dependency import InflationFixingDependency

# TODO update the JSON string below
json = "{}"
# create an instance of InflationFixingDependency from a JSON string
inflation_fixing_dependency_instance = InflationFixingDependency.from_json(json)
# print the JSON string representation of the object
print InflationFixingDependency.to_json()

# convert the object into a dict
inflation_fixing_dependency_dict = inflation_fixing_dependency_instance.to_dict()
# create an instance of InflationFixingDependency from a dict
inflation_fixing_dependency_form_dict = inflation_fixing_dependency.from_dict(inflation_fixing_dependency_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


