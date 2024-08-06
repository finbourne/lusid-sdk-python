# DayMonth


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**day** | **int** | Day part of Day, Month for Year End date specification. | 
**month** | **int** | Month part of Day, Month for Year End date specification. | 

## Example

```python
from lusid.models.day_month import DayMonth

# TODO update the JSON string below
json = "{}"
# create an instance of DayMonth from a JSON string
day_month_instance = DayMonth.from_json(json)
# print the JSON string representation of the object
print DayMonth.to_json()

# convert the object into a dict
day_month_dict = day_month_instance.to_dict()
# create an instance of DayMonth from a dict
day_month_form_dict = day_month.from_dict(day_month_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


