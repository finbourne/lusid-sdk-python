# LockPeriodDiaryEntryRequest

A definition for the period you wish to lock

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**diary_entry_code** | **str** | Unique code assigned to a period. When left blank last closed period will be located. | [optional] 
**closing_options** | **List[str]** | The options which will be executed once a period is closed or locked. | [optional] 

## Example

```python
from lusid.models.lock_period_diary_entry_request import LockPeriodDiaryEntryRequest

# TODO update the JSON string below
json = "{}"
# create an instance of LockPeriodDiaryEntryRequest from a JSON string
lock_period_diary_entry_request_instance = LockPeriodDiaryEntryRequest.from_json(json)
# print the JSON string representation of the object
print LockPeriodDiaryEntryRequest.to_json()

# convert the object into a dict
lock_period_diary_entry_request_dict = lock_period_diary_entry_request_instance.to_dict()
# create an instance of LockPeriodDiaryEntryRequest from a dict
lock_period_diary_entry_request_form_dict = lock_period_diary_entry_request.from_dict(lock_period_diary_entry_request_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


