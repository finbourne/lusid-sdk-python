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
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, conlist

pnl_bucket: Optional[StrictStr] = "example_pnl_bucket"
journal_entry_line: Optional[JournalEntryLine] = # Replace with your value
links: Optional[conlist(Link)] = None
pnl_journal_entry_line_instance = PnlJournalEntryLine(pnl_bucket=pnl_bucket, journal_entry_line=journal_entry_line, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

