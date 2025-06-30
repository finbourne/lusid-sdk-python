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
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, conlist, constr, validator

start: Optional[DateOrDiaryEntry] = None
end: Optional[DateOrDiaryEntry] = None
date_mode: Optional[StrictStr] = "example_date_mode"
general_ledger_profile_code: Optional[StrictStr] = "example_general_ledger_profile_code"
property_keys: Optional[conlist(StrictStr)] = # Replace with your value
journal_entry_lines_query_parameters_instance = JournalEntryLinesQueryParameters(start=start, end=end, date_mode=date_mode, general_ledger_profile_code=general_ledger_profile_code, property_keys=property_keys)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

