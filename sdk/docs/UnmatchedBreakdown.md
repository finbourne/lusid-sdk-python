# UnmatchedBreakdown

What a reserved unmatched sub-bucket holds: the amount routed to it and how many journal entry lines matched no  bucket filter to produce it.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**no_filter_match** | **float** | The amount in the bucket over the period from journal entry lines that matched no bucket&#39;s filter. | 
**no_filter_match_count** | **int** | How many journal entry lines produced that amount. On a share class node it counts the lines booked to the class and the fund-level and allocation group lines it takes a share of; on the fund node it counts every line once. | 
## Example

```python
from lusid.models.unmatched_breakdown import UnmatchedBreakdown
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

no_filter_match: Union[StrictFloat, StrictInt] = # Replace with your value
no_filter_match_count: StrictInt = # Replace with your value
no_filter_match_count: StrictInt = 42
unmatched_breakdown_instance = UnmatchedBreakdown(no_filter_match=no_filter_match, no_filter_match_count=no_filter_match_count)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

