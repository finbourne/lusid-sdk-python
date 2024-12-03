# PnlJournalEntryLine


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pnl_bucket** | **str** | The Filter ID of the grouping used from the Fund Configuration PnL filters | [optional] 
**journal_entry_line** | [**JournalEntryLine**](JournalEntryLine.md) |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.pnl_journal_entry_line import PnlJournalEntryLine

# TODO update the JSON string below
json = "{}"
# create an instance of PnlJournalEntryLine from a JSON string
pnl_journal_entry_line_instance = PnlJournalEntryLine.from_json(json)
# print the JSON string representation of the object
print PnlJournalEntryLine.to_json()

# convert the object into a dict
pnl_journal_entry_line_dict = pnl_journal_entry_line_instance.to_dict()
# create an instance of PnlJournalEntryLine from a dict
pnl_journal_entry_line_form_dict = pnl_journal_entry_line.from_dict(pnl_journal_entry_line_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


