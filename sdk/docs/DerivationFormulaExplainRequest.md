# DerivationFormulaExplainRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_type** | **str** | The type of the entity for which the derived property or partial formula is to be resolved against. | 
**scope** | **str** | (Optional) The scope that entity exists in. If no scope is provided, the default scope for the entity type will be used. | [optional] 
**code** | **str** | (Optional) The code of the entity, to be provided for entities that support scope/code retrieval. If no code or identifier is provided, the logical evaluation tree without resolved values is returned. | [optional] 
**identifier** | **Dict[str, str]** | (Optional). An identifier key/value pair that uniquely identifies the entity to explain the derived property for. This can be either an instrument identifier, or an identifier property. If no code or identifier is provided, the logical evaluation tree without resolved values is returned. | [optional] 
**property_key** | **str** | (Optional) The key of the derived property to get an explanation for. This takes the format {domain}/{scope}/{code}. One of either property key or partial formula must be provided. | [optional] 
**partial_formula** | **str** | (Optional) A partial derivation formula to get an explanation for. Can be provided in lieu of a property key. One of either property key or partial formula must be provided. | [optional] 
## Example

```python
from lusid.models.derivation_formula_explain_request import DerivationFormulaExplainRequest
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, constr, validator

entity_type: StrictStr = "example_entity_type"
scope: Optional[StrictStr] = "example_scope"
code: Optional[StrictStr] = "example_code"
identifier: Optional[Dict[str, StrictStr]] = # Replace with your value
property_key: Optional[StrictStr] = "example_property_key"
partial_formula: Optional[StrictStr] = "example_partial_formula"
derivation_formula_explain_request_instance = DerivationFormulaExplainRequest(entity_type=entity_type, scope=scope, code=code, identifier=identifier, property_key=property_key, partial_formula=partial_formula)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

