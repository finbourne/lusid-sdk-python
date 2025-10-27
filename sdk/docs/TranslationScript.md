# TranslationScript

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**TranslationScriptId**](TranslationScriptId.md) |  | 
**body** | **str** | Body of the translation script, i.e. the actual translation code. | 
**version** | [**Version**](Version.md) |  | [optional] 
## Example

```python
from lusid.models.translation_script import TranslationScript
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

id: TranslationScriptId
body: StrictStr = "example_body"
version: Optional[Version] = None
translation_script_instance = TranslationScript(id=id, body=body, version=version)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

