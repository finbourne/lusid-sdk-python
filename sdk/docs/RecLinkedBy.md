# RecLinkedBy

The item pairings a link between two rec results was established on, per side.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**left** | [**List[RecResultLinkKey]**](RecResultLinkKey.md) | The pairings between the two results&#39; left-side items, one entry per pairing. May be empty. | 
**right** | [**List[RecResultLinkKey]**](RecResultLinkKey.md) | The pairings between the two results&#39; right-side items, one entry per pairing. May be empty. | 
## Example

```python
from lusid.models.rec_linked_by import RecLinkedBy
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

left: List[RecResultLinkKey] = # Replace with your value
right: List[RecResultLinkKey] = # Replace with your value
rec_linked_by_instance = RecLinkedBy(left=left, right=right)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

