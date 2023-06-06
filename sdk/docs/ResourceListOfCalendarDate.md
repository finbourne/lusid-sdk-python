# ResourceListOfCalendarDate


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | [**List[CalendarDate]**](CalendarDate.md) |  | 
**href** | **str** |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
**next_page** | **str** |  | [optional] 
**previous_page** | **str** |  | [optional] 

## Example

```python
from lusid.models.resource_list_of_calendar_date import ResourceListOfCalendarDate

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceListOfCalendarDate from a JSON string
resource_list_of_calendar_date_instance = ResourceListOfCalendarDate.from_json(json)
# print the JSON string representation of the object
print ResourceListOfCalendarDate.to_json()

# convert the object into a dict
resource_list_of_calendar_date_dict = resource_list_of_calendar_date_instance.to_dict()
# create an instance of ResourceListOfCalendarDate from a dict
resource_list_of_calendar_date_form_dict = resource_list_of_calendar_date.from_dict(resource_list_of_calendar_date_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


