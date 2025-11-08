# DerivationFormulaExplainRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_type** | **str** | The type of the entity for which the derived property or partial formula is to be resolved against. | 
**scope** | **str** | (Optional) The scope that entity exists in. If no scope is provided, the default scope for the entity type will be used. | [optional] 
**code** | **str** | (Optional) The code of the entity, to be provided for entities that support scope/code retrieval. If no code or identifier is provided, the logical evaluation tree without resolved values is returned. | [optional] 
**subentity_id** | **str** | (Optional) The id of the sub-entity to explain the derived property for. This must be provided along with the scope/code of the parent entity. | [optional] 
**identifier** | **Dict[str, Optional[str]]** | (Optional). An identifier key/value pair that uniquely identifies the entity to explain the derived property for. This can be either an instrument identifier, or an identifier property. If no code or identifier is provided, the logical evaluation tree without resolved values is returned. | [optional] 
**property_key** | **str** | (Optional) The key of the derived property to get an explanation for. This takes the format {domain}/{scope}/{code}. One of either property key or partial formula must be provided. | [optional] 
**partial_formula** | **str** | (Optional) A partial derivation formula to get an explanation for. Can be provided in lieu of a property key. One of either property key or partial formula must be provided. | [optional] 
## Example

```python
from lusid.models.derivation_formula_explain_request import DerivationFormulaExplainRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

entity_type: StrictStr = "example_entity_type"
scope: Optional[StrictStr] = "example_scope"
code: Optional[StrictStr] = "example_code"
subentity_id: Optional[StrictStr] = "example_subentity_id"
identifier: Optional[Dict[str, Optional[StrictStr]]] = # Replace with your value
property_key: Optional[StrictStr] = "example_property_key"
partial_formula: Optional[StrictStr] = "example_partial_formula"
derivation_formula_explain_request_instance = DerivationFormulaExplainRequest(entity_type=entity_type, scope=scope, code=code, subentity_id=subentity_id, identifier=identifier, property_key=property_key, partial_formula=partial_formula)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

