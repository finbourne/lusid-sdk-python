# UpsertTranslationScriptRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**TranslationScriptId**](TranslationScriptId.md) |  | 
**body** | **str** | Body of the translation script, i.e. the actual translation code. | 
## Example

```python
from lusid.models.upsert_translation_script_request import UpsertTranslationScriptRequest
from typing import Any, Dict
from pydantic.v1 import BaseModel, Field, constr

id: TranslationScriptId = # Replace with your value
body: StrictStr = "example_body"
upsert_translation_script_request_instance = UpsertTranslationScriptRequest(id=id, body=body)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

