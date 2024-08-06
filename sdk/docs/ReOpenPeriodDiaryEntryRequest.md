# ReOpenPeriodDiaryEntryRequest

A definition for the period you wish to re open

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**diary_entry_code** | **str** | Unique code assigned to a period. When left blank last period will be used. | [optional] 

## Example

```python
from lusid.models.re_open_period_diary_entry_request import ReOpenPeriodDiaryEntryRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReOpenPeriodDiaryEntryRequest from a JSON string
re_open_period_diary_entry_request_instance = ReOpenPeriodDiaryEntryRequest.from_json(json)
# print the JSON string representation of the object
print ReOpenPeriodDiaryEntryRequest.to_json()

# convert the object into a dict
re_open_period_diary_entry_request_dict = re_open_period_diary_entry_request_instance.to_dict()
# create an instance of ReOpenPeriodDiaryEntryRequest from a dict
re_open_period_diary_entry_request_form_dict = re_open_period_diary_entry_request.from_dict(re_open_period_diary_entry_request_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


