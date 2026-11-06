# InitialMarginChange

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**we_post_before** | **float** | What we must post to the set today, after the threshold. | 
**we_post_after** | **float** | What we would post to the set after the move, after the threshold. | 
**they_post_before** | **float** | What the counterparty must post today. Null where the run does not know it, as under SIMM without their sensitivities. | [optional] 
**they_post_after** | **float** | What the counterparty would post after the move. Null where the run does not know it. | [optional] 
## Example

```python
from lusid.models.initial_margin_change import InitialMarginChange
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

we_post_before: Union[StrictFloat, StrictInt] = # Replace with your value
we_post_after: Union[StrictFloat, StrictInt] = # Replace with your value
they_post_before: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
they_post_after: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
initial_margin_change_instance = InitialMarginChange(we_post_before=we_post_before, we_post_after=we_post_after, they_post_before=they_post_before, they_post_after=they_post_after)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

