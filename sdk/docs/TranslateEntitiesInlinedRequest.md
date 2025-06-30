# TranslateEntitiesInlinedRequest

Request to translate financial entities with a given script body.  The output of the translation is validated against a schema specified in the request.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_payloads** | [**Dict[str, TranslationInput]**](TranslationInput.md) | Entity payloads to be translated indexed by (ephemeral) unique correlation ids. | 
**script_body** | **str** | The body of the translation script to use for translating the entities. | 
**var_schema** | [**DialectSchema**](DialectSchema.md) |  | [optional] 
## Example

```python
from lusid.models.translate_entities_inlined_request import TranslateEntitiesInlinedRequest
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, constr

entity_payloads: Dict[str, TranslationInput] = # Replace with your value
script_body: StrictStr = "example_script_body"
var_schema: Optional[DialectSchema] = # Replace with your value
translate_entities_inlined_request_instance = TranslateEntitiesInlinedRequest(entity_payloads=entity_payloads, script_body=script_body, var_schema=var_schema)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

