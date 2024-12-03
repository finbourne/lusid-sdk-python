# ValuationPointResourceListOfPnlJournalEntryLine

ResourceList with extra header fields used by the various ValuationPoint endpoints for returning additional context related to the list of results.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_valuation_point** | [**DiaryEntry**](DiaryEntry.md) |  | [optional] 
**version** | [**Version**](Version.md) |  | 
**values** | [**List[PnlJournalEntryLine]**](PnlJournalEntryLine.md) |  | 
**href** | **str** |  | [optional] 
**next_page** | **str** |  | [optional] 
**previous_page** | **str** |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.valuation_point_resource_list_of_pnl_journal_entry_line import ValuationPointResourceListOfPnlJournalEntryLine

# TODO update the JSON string below
json = "{}"
# create an instance of ValuationPointResourceListOfPnlJournalEntryLine from a JSON string
valuation_point_resource_list_of_pnl_journal_entry_line_instance = ValuationPointResourceListOfPnlJournalEntryLine.from_json(json)
# print the JSON string representation of the object
print ValuationPointResourceListOfPnlJournalEntryLine.to_json()

# convert the object into a dict
valuation_point_resource_list_of_pnl_journal_entry_line_dict = valuation_point_resource_list_of_pnl_journal_entry_line_instance.to_dict()
# create an instance of ValuationPointResourceListOfPnlJournalEntryLine from a dict
valuation_point_resource_list_of_pnl_journal_entry_line_form_dict = valuation_point_resource_list_of_pnl_journal_entry_line.from_dict(valuation_point_resource_list_of_pnl_journal_entry_line_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


