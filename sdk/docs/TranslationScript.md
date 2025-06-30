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
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, constr

id: TranslationScriptId = # Replace with your value
body: StrictStr = "example_body"
version: Optional[Version] = None
translation_script_instance = TranslationScript(id=id, body=body, version=version)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

