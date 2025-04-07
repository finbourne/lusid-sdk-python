# YearMonthDay

A date in component form.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**year** | **int** | The year of the date. | 
**month** | **int** | The month of the date. | 
**day** | **int** | The day in month of the date. | 

## Example

```python
from lusid.models.year_month_day import YearMonthDay

# TODO update the JSON string below
json = "{}"
# create an instance of YearMonthDay from a JSON string
year_month_day_instance = YearMonthDay.from_json(json)
# print the JSON string representation of the object
print YearMonthDay.to_json()

# convert the object into a dict
year_month_day_dict = year_month_day_instance.to_dict()
# create an instance of YearMonthDay from a dict
year_month_day_form_dict = year_month_day.from_dict(year_month_day_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


