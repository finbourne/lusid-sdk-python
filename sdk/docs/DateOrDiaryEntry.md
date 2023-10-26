# DateOrDiaryEntry


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **str** | A date. If specified, DiaryEntry must not be specified. | [optional] 
**diary_entry** | **str** | The code of a diary entry. If specified, Date must not be specified. | [optional] 

## Example

```python
from lusid.models.date_or_diary_entry import DateOrDiaryEntry

# TODO update the JSON string below
json = "{}"
# create an instance of DateOrDiaryEntry from a JSON string
date_or_diary_entry_instance = DateOrDiaryEntry.from_json(json)
# print the JSON string representation of the object
print DateOrDiaryEntry.to_json()

# convert the object into a dict
date_or_diary_entry_dict = date_or_diary_entry_instance.to_dict()
# create an instance of DateOrDiaryEntry from a dict
date_or_diary_entry_form_dict = date_or_diary_entry.from_dict(date_or_diary_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


