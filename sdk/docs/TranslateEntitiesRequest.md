# TranslateEntitiesRequest

Request to translate financial entities with a specified script stored in LUSID, specified in the request by its id. The output of the translation is validated against a dialect stored in LUSID, again specified in the request by its id.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_payloads** | [**Dict[str, TranslationInput]**](TranslationInput.md) | Entity payloads to be translated, indexed by (ephemeral) unique correlation ids. | 
**script_id** | [**TranslationScriptId**](TranslationScriptId.md) |  | 
**dialect_id** | [**DialectId**](DialectId.md) |  | [optional] 
## Example

```python
from lusid.models.translate_entities_request import TranslateEntitiesRequest
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field

entity_payloads: Dict[str, TranslationInput] = # Replace with your value
script_id: TranslationScriptId = # Replace with your value
dialect_id: Optional[DialectId] = # Replace with your value
translate_entities_request_instance = TranslateEntitiesRequest(entity_payloads=entity_payloads, script_id=script_id, dialect_id=dialect_id)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

