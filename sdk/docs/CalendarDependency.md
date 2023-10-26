# CalendarDependency

For indicating a dependency upon calendar codes

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**calendars** | **List[str]** | The Codes of the calendars that are depended upon. | 
**dependency_type** | **str** | The available values are: OpaqueDependency, CashDependency, DiscountingDependency, EquityCurveDependency, EquityVolDependency, FxDependency, FxForwardsDependency, FxVolDependency, IndexProjectionDependency, IrVolDependency, QuoteDependency, Vendor, CalendarDependency, InflationFixingDependency | 

## Example

```python
from lusid.models.calendar_dependency import CalendarDependency

# TODO update the JSON string below
json = "{}"
# create an instance of CalendarDependency from a JSON string
calendar_dependency_instance = CalendarDependency.from_json(json)
# print the JSON string representation of the object
print CalendarDependency.to_json()

# convert the object into a dict
calendar_dependency_dict = calendar_dependency_instance.to_dict()
# create an instance of CalendarDependency from a dict
calendar_dependency_form_dict = calendar_dependency.from_dict(calendar_dependency_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


