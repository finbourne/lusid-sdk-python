# QueryFundCashStatementParameters

Request body for querying a Fund Cash Statement.  Extends the diary entry query pattern with cash statement display mode.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start** | [**DateOrDiaryEntry**](DateOrDiaryEntry.md) |  | [optional] 
**end** | [**DateOrDiaryEntry**](DateOrDiaryEntry.md) |  | 
**variant** | **str** | Optional diary entry variant (e.g. for multi-estimate scenarios). | [optional] 
**display_mode** | **str** | Cash statement display mode: ShowReversal (default) shows full reversal/TrueUp detail; Consolidated collapses reversals into AvgRateCorrection rows. | [optional] 
## Example

```python
from lusid.models.query_fund_cash_statement_parameters import QueryFundCashStatementParameters
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

start: Optional[DateOrDiaryEntry] = None
end: DateOrDiaryEntry
variant: Optional[StrictStr] = "example_variant"
display_mode: Optional[StrictStr] = "example_display_mode"
query_fund_cash_statement_parameters_instance = QueryFundCashStatementParameters(start=start, end=end, variant=variant, display_mode=display_mode)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

