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
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

start_valuation_point: Optional[DiaryEntry] = # Replace with your value
version: Version
values: List[PnlJournalEntryLine]
href: Optional[StrictStr] = "example_href"
next_page: Optional[StrictStr] = "example_next_page"
previous_page: Optional[StrictStr] = "example_previous_page"
links: Optional[List[Link]] = None
valuation_point_resource_list_of_pnl_journal_entry_line_instance = ValuationPointResourceListOfPnlJournalEntryLine(start_valuation_point=start_valuation_point, version=version, values=values, href=href, next_page=next_page, previous_page=previous_page, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

