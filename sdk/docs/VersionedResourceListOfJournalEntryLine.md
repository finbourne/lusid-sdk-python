# VersionedResourceListOfJournalEntryLine


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | [**Version**](Version.md) |  | 
**values** | [**List[JournalEntryLine]**](JournalEntryLine.md) |  | 
**href** | **str** |  | [optional] 
**next_page** | **str** |  | [optional] 
**previous_page** | **str** |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.versioned_resource_list_of_journal_entry_line import VersionedResourceListOfJournalEntryLine

# TODO update the JSON string below
json = "{}"
# create an instance of VersionedResourceListOfJournalEntryLine from a JSON string
versioned_resource_list_of_journal_entry_line_instance = VersionedResourceListOfJournalEntryLine.from_json(json)
# print the JSON string representation of the object
print VersionedResourceListOfJournalEntryLine.to_json()

# convert the object into a dict
versioned_resource_list_of_journal_entry_line_dict = versioned_resource_list_of_journal_entry_line_instance.to_dict()
# create an instance of VersionedResourceListOfJournalEntryLine from a dict
versioned_resource_list_of_journal_entry_line_form_dict = versioned_resource_list_of_journal_entry_line.from_dict(versioned_resource_list_of_journal_entry_line_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


