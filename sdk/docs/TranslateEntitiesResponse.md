# TranslateEntitiesResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | [**Dict[str, TranslationResult]**](TranslationResult.md) | The entities that were successfully translated. | [optional] 
**failed** | [**Dict[str, ErrorDetail]**](ErrorDetail.md) | The error details corresponding to entities that failed to be translated. | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.translate_entities_response import TranslateEntitiesResponse
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

values: Optional[Dict[str, TranslationResult]] = # Replace with your value
failed: Optional[Dict[str, ErrorDetail]] = # Replace with your value
links: Optional[List[Link]] = None
translate_entities_response_instance = TranslateEntitiesResponse(values=values, failed=failed, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

