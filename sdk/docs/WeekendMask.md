# WeekendMask


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**days** | [**List[DayOfWeek]**](DayOfWeek.md) |  | 
**time_zone** | **str** |  | 

## Example

```python
from lusid.models.weekend_mask import WeekendMask

# TODO update the JSON string below
json = "{}"
# create an instance of WeekendMask from a JSON string
weekend_mask_instance = WeekendMask.from_json(json)
# print the JSON string representation of the object
print WeekendMask.to_json()

# convert the object into a dict
weekend_mask_dict = weekend_mask_instance.to_dict()
# create an instance of WeekendMask from a dict
weekend_mask_form_dict = weekend_mask.from_dict(weekend_mask_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


