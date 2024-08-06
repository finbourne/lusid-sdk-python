# VendorDependency

For indicating a dependency on some opaque market data requested by an outside vendor

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vendor_name** | **str** | The name of the outside vendor | 
**vendor_path** | **List[str]** | The specific dependency path | 
**var_date** | **datetime** | The effectiveDate of the entity that this is a dependency for. | 
**dependency_type** | **str** | The available values are: OpaqueDependency, CashDependency, DiscountingDependency, EquityCurveDependency, EquityVolDependency, FxDependency, FxForwardsDependency, FxVolDependency, IndexProjectionDependency, IrVolDependency, QuoteDependency, Vendor, CalendarDependency, InflationFixingDependency | 

## Example

```python
from lusid.models.vendor_dependency import VendorDependency

# TODO update the JSON string below
json = "{}"
# create an instance of VendorDependency from a JSON string
vendor_dependency_instance = VendorDependency.from_json(json)
# print the JSON string representation of the object
print VendorDependency.to_json()

# convert the object into a dict
vendor_dependency_dict = vendor_dependency_instance.to_dict()
# create an instance of VendorDependency from a dict
vendor_dependency_form_dict = vendor_dependency.from_dict(vendor_dependency_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


