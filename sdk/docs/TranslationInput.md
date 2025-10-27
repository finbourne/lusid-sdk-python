# TranslationInput

The input to a translation script.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity** | **str** | The serialised entity to be passed to the translation script. This could represent e.g. an instrument in any  dialect. | 
## Example

```python
from lusid.models.translation_input import TranslationInput
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

entity: StrictStr = "example_entity"
translation_input_instance = TranslationInput(entity=entity)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

