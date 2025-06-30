# TranslationContext

Options for overriding default scripted translation configuration.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disable_scripted_translation** | **bool** |  | [optional] 
**script_map** | [**ScriptMapReference**](ScriptMapReference.md) |  | [optional] 
## Example

```python
from lusid.models.translation_context import TranslationContext
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, StrictBool

disable_scripted_translation: Optional[StrictBool] = # Replace with your value
disable_scripted_translation:Optional[StrictBool] = None
script_map: Optional[ScriptMapReference] = # Replace with your value
translation_context_instance = TranslationContext(disable_scripted_translation=disable_scripted_translation, script_map=script_map)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

