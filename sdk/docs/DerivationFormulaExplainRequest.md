# DerivationFormulaExplainRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_type** | **str** | The type of the entity for which the derived property or partial formula is to be resolved against. | 
**scope** | **str** | The scope that entity exists in. If no scope is provided, the default scope for the entity type will be used. | [optional] 
**identifier** | **Dict[str, str]** | An identifier key/value pair that uniquely identifies the entity to explain the derived property for. This can be either an instrument identifier, an identifier property, or a scope/code identifier which take the format {entityType}/default/code : {identifier}. If no identifiers are provided, the logical evaluation tree without resolved values is returned. | [optional] 
**property_key** | **str** | The key of the derived property to explain. This takes the format {domain}/{scope}/{code}. | [optional] 
**partial_formula** | **str** | A partial derivation formula to explain. Can be provided in lieu of a property key. | [optional] 
## Example

```python
from lusid.models.derivation_formula_explain_request import DerivationFormulaExplainRequest
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, constr, validator

entity_type: StrictStr = "example_entity_type"
scope: Optional[StrictStr] = "example_scope"
identifier: Optional[Dict[str, StrictStr]] = # Replace with your value
property_key: Optional[StrictStr] = "example_property_key"
partial_formula: Optional[StrictStr] = "example_partial_formula"
derivation_formula_explain_request_instance = DerivationFormulaExplainRequest(entity_type=entity_type, scope=scope, identifier=identifier, property_key=property_key, partial_formula=partial_formula)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

