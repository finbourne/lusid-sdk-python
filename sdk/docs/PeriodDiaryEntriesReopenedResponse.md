# PeriodDiaryEntriesReopenedResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**effective_from** | **datetime** | The effective datetime at which the deletion became valid. May be null in the case where multiple date times are applicable. | [optional] 
**as_at** | **datetime** | The asAt datetime at which the deletion was committed to LUSID. | 
**period_diary_entries_removed** | **int** | Number of Diary Entries removed as a result of reopening periods | 
**period_diary_entries_from** | **datetime** | The start point where periods were removed from | 
**period_diary_entries_to** | **datetime** | The end point where periods were removed to | 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.period_diary_entries_reopened_response import PeriodDiaryEntriesReopenedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PeriodDiaryEntriesReopenedResponse from a JSON string
period_diary_entries_reopened_response_instance = PeriodDiaryEntriesReopenedResponse.from_json(json)
# print the JSON string representation of the object
print PeriodDiaryEntriesReopenedResponse.to_json()

# convert the object into a dict
period_diary_entries_reopened_response_dict = period_diary_entries_reopened_response_instance.to_dict()
# create an instance of PeriodDiaryEntriesReopenedResponse from a dict
period_diary_entries_reopened_response_form_dict = period_diary_entries_reopened_response.from_dict(period_diary_entries_reopened_response_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


