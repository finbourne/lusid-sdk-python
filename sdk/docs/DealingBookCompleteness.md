# DealingBookCompleteness

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**complete** | **bool** | Whether every share class&#39;s dealing cut-off had passed at the strike&#39;s as-at. True when no cut-off is configured. | 
**cut_off** | **datetime** | The latest dealing cut-off among the share classes that configure one. Absent when none does. | [optional] 
**late_not_counted** | **int** | How many orders at the valuation point were written to the book after their class&#39;s cut-off and so were reported but not counted. Absent when a cut-off is configured but lateness could not be judged because an order at the valuation point carries no version. | [optional] 
**note** | **str** | Why the book was judged complete or incomplete: the cut-off that had or had not passed, or that none is configured and completeness was assumed. | [optional] 
## Example

```python
from lusid.models.dealing_book_completeness import DealingBookCompleteness
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

complete: StrictBool = # Replace with your value
complete:StrictBool = True
cut_off: Optional[datetime] = # Replace with your value
late_not_counted: Optional[StrictInt] = # Replace with your value
late_not_counted: Optional[StrictInt] = None
note: Optional[StrictStr] = "example_note"
dealing_book_completeness_instance = DealingBookCompleteness(complete=complete, cut_off=cut_off, late_not_counted=late_not_counted, note=note)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

