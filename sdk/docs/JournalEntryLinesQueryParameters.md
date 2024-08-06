# JournalEntryLinesQueryParameters


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start** | [**DateOrDiaryEntry**](DateOrDiaryEntry.md) |  | [optional] 
**end** | [**DateOrDiaryEntry**](DateOrDiaryEntry.md) |  | [optional] 
**date_mode** | **str** | The mode of calculation of the journal entry lines. The available values are: ActivityDate, AccountingDate. | [optional] 
**general_ledger_profile_code** | **str** | The optional code of a general ledger profile used to decorate journal entry lines with levels. | [optional] 
**property_keys** | **List[str]** | A list of property keys from the &#39;Instrument&#39;, &#39;Transaction&#39;, &#39;Portfolio&#39;, &#39;Account&#39;, &#39;LegalEntity&#39; or &#39;CustodianAccount&#39; domain to decorate onto the journal entry lines. | [optional] 

## Example

```python
from lusid.models.journal_entry_lines_query_parameters import JournalEntryLinesQueryParameters

# TODO update the JSON string below
json = "{}"
# create an instance of JournalEntryLinesQueryParameters from a JSON string
journal_entry_lines_query_parameters_instance = JournalEntryLinesQueryParameters.from_json(json)
# print the JSON string representation of the object
print JournalEntryLinesQueryParameters.to_json()

# convert the object into a dict
journal_entry_lines_query_parameters_dict = journal_entry_lines_query_parameters_instance.to_dict()
# create an instance of JournalEntryLinesQueryParameters from a dict
journal_entry_lines_query_parameters_form_dict = journal_entry_lines_query_parameters.from_dict(journal_entry_lines_query_parameters_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


