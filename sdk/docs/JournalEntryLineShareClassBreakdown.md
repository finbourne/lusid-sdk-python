# JournalEntryLineShareClassBreakdown

The apportionment from overall fund level journal entry Line to the share class.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**short_code** | **str** | The share class identifier. | [optional] 
**apportionment_factor** | **float** | The share class apportionment factor (capital ratio). | [optional] 
**local_value** | **float** | This journal entry line&#39;s local value amount after apportionment is applied. | [optional] 
**base_value** | **float** | This journal entry line&#39;s base value amount after apportionment is applied | [optional] 

## Example

```python
from lusid.models.journal_entry_line_share_class_breakdown import JournalEntryLineShareClassBreakdown

# TODO update the JSON string below
json = "{}"
# create an instance of JournalEntryLineShareClassBreakdown from a JSON string
journal_entry_line_share_class_breakdown_instance = JournalEntryLineShareClassBreakdown.from_json(json)
# print the JSON string representation of the object
print JournalEntryLineShareClassBreakdown.to_json()

# convert the object into a dict
journal_entry_line_share_class_breakdown_dict = journal_entry_line_share_class_breakdown_instance.to_dict()
# create an instance of JournalEntryLineShareClassBreakdown from a dict
journal_entry_line_share_class_breakdown_form_dict = journal_entry_line_share_class_breakdown.from_dict(journal_entry_line_share_class_breakdown_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


