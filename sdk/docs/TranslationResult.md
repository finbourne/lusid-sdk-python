# TranslationResult

The result of invoking a translation script.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity** | **str** | The serialised entity the translation script produced. | 
**properties** | [**Dict[str, ModelProperty]**](ModelProperty.md) | Any properties the translation script produced. | 
## Example

```python
from lusid.models.translation_result import TranslationResult
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

entity: StrictStr = "example_entity"
properties: Dict[str, ModelProperty] = # Replace with your value
translation_result_instance = TranslationResult(entity=entity, properties=properties)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

