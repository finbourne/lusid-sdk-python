# RecLinkKey

One item key that established a link between two rec results: the key name and the identifier value both  results' items carried for it.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The key name: holdingId or transactionId. | 
**value** | **str** | The identifier value both results&#39; items carried under the key. | 
## Example

```python
from lusid.models.rec_link_key import RecLinkKey
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

key: StrictStr = "example_key"
value: StrictStr = "example_value"
rec_link_key_instance = RecLinkKey(key=key, value=value)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

