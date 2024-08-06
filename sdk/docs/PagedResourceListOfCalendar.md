# PagedResourceListOfCalendar


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next_page** | **str** |  | [optional] 
**previous_page** | **str** |  | [optional] 
**values** | [**List[Calendar]**](Calendar.md) |  | 
**href** | **str** |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.paged_resource_list_of_calendar import PagedResourceListOfCalendar

# TODO update the JSON string below
json = "{}"
# create an instance of PagedResourceListOfCalendar from a JSON string
paged_resource_list_of_calendar_instance = PagedResourceListOfCalendar.from_json(json)
# print the JSON string representation of the object
print PagedResourceListOfCalendar.to_json()

# convert the object into a dict
paged_resource_list_of_calendar_dict = paged_resource_list_of_calendar_instance.to_dict()
# create an instance of PagedResourceListOfCalendar from a dict
paged_resource_list_of_calendar_form_dict = paged_resource_list_of_calendar.from_dict(paged_resource_list_of_calendar_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


