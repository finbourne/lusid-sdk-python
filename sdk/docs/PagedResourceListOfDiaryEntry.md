# PagedResourceListOfDiaryEntry


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next_page** | **str** |  | [optional] 
**previous_page** | **str** |  | [optional] 
**values** | [**List[DiaryEntry]**](DiaryEntry.md) |  | 
**href** | **str** |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.paged_resource_list_of_diary_entry import PagedResourceListOfDiaryEntry

# TODO update the JSON string below
json = "{}"
# create an instance of PagedResourceListOfDiaryEntry from a JSON string
paged_resource_list_of_diary_entry_instance = PagedResourceListOfDiaryEntry.from_json(json)
# print the JSON string representation of the object
print PagedResourceListOfDiaryEntry.to_json()

# convert the object into a dict
paged_resource_list_of_diary_entry_dict = paged_resource_list_of_diary_entry_instance.to_dict()
# create an instance of PagedResourceListOfDiaryEntry from a dict
paged_resource_list_of_diary_entry_form_dict = paged_resource_list_of_diary_entry.from_dict(paged_resource_list_of_diary_entry_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


