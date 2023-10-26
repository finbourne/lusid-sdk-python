# BucketingSchedule

A schedule for dates

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenor** | **str** | Rolling tenor | [optional] 

## Example

```python
from lusid.models.bucketing_schedule import BucketingSchedule

# TODO update the JSON string below
json = "{}"
# create an instance of BucketingSchedule from a JSON string
bucketing_schedule_instance = BucketingSchedule.from_json(json)
# print the JSON string representation of the object
print BucketingSchedule.to_json()

# convert the object into a dict
bucketing_schedule_dict = bucketing_schedule_instance.to_dict()
# create an instance of BucketingSchedule from a dict
bucketing_schedule_form_dict = bucketing_schedule.from_dict(bucketing_schedule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


