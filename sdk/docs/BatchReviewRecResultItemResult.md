# BatchReviewRecResultItemResult

The successful outcome of a single batch review item: every rec result affected by the item (which  may exceed the results named in the request, e.g. group members re-opened by a nullify).
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rec_results** | [**List[RecResult]**](RecResult.md) | The full set of rec results affected by the batch item (may exceed the results named in the request). | 
## Example

```python
from lusid.models.batch_review_rec_result_item_result import BatchReviewRecResultItemResult
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

rec_results: List[RecResult] = # Replace with your value
batch_review_rec_result_item_result_instance = BatchReviewRecResultItemResult(rec_results=rec_results)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

