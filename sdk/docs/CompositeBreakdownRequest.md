# CompositeBreakdownRequest

The request used in the GetCompositeBreakdown.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**return_ids** | [**List[ResourceId]**](ResourceId.md) | The Scope and code of the returns. | [optional] 
**recipe_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**composite_method** | **str** | The method used to calculate the Portfolio performance: Equal/Asset. | [optional] 
**period** | **str** | The type of the returns used to calculate the aggregation result: Daily/Monthly. | [optional] 
**holiday_calendars** | **List[str]** | The holiday calendar(s) that should be used in determining the date schedule. Holiday calendar(s) are supplied by their codes, for example, &#39;CoppClark&#39;. Note that when the calendars are not available (e.g. when the user has insufficient permissions), a recipe setting will be used to determine whether the whole batch should then fail or whether the calendar not being available should simply be ignored. | [optional] 
**currency** | **str** | Optional - either a string or a property. If provided, the results will be converted to the specified currency | [optional] 

## Example

```python
from lusid.models.composite_breakdown_request import CompositeBreakdownRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CompositeBreakdownRequest from a JSON string
composite_breakdown_request_instance = CompositeBreakdownRequest.from_json(json)
# print the JSON string representation of the object
print CompositeBreakdownRequest.to_json()

# convert the object into a dict
composite_breakdown_request_dict = composite_breakdown_request_instance.to_dict()
# create an instance of CompositeBreakdownRequest from a dict
composite_breakdown_request_form_dict = composite_breakdown_request.from_dict(composite_breakdown_request_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


