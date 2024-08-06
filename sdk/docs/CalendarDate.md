# CalendarDate


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** |  | [optional] 
**date_identifier** | **str** |  | 
**from_utc** | **datetime** |  | 
**to_utc** | **datetime** |  | 
**local_date** | **str** |  | 
**timezone** | **str** |  | 
**description** | **str** |  | 
**type** | **str** |  | 
**attributes** | [**DateAttributes**](DateAttributes.md) |  | [optional] 
**source_data** | **Dict[str, str]** |  | [optional] 

## Example

```python
from lusid.models.calendar_date import CalendarDate

# TODO update the JSON string below
json = "{}"
# create an instance of CalendarDate from a JSON string
calendar_date_instance = CalendarDate.from_json(json)
# print the JSON string representation of the object
print CalendarDate.to_json()

# convert the object into a dict
calendar_date_dict = calendar_date_instance.to_dict()
# create an instance of CalendarDate from a dict
calendar_date_form_dict = calendar_date.from_dict(calendar_date_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


