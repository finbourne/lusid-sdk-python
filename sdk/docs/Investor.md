# Investor

Representation of an Investor on the LUSID API
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**investor_type** | **str** | The type of the Investor | [optional] 
**investor_identifiers** | [**Dict[str, ModelProperty]**](ModelProperty.md) | The identifiers of the Investor | [optional] 
**entity_unique_id** | **str** | The unique Investor entity identifier | [optional] 
**person** | [**Person**](Person.md) |  | [optional] 
**legal_entity** | [**LegalEntity**](LegalEntity.md) |  | [optional] 
## Example

```python
from lusid.models.investor import Investor
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, StrictStr

investor_type: Optional[StrictStr] = "example_investor_type"
investor_identifiers: Optional[Dict[str, ModelProperty]] = # Replace with your value
entity_unique_id: Optional[StrictStr] = "example_entity_unique_id"
person: Optional[Person] = None
legal_entity: Optional[LegalEntity] = # Replace with your value
investor_instance = Investor(investor_type=investor_type, investor_identifiers=investor_identifiers, entity_unique_id=entity_unique_id, person=person, legal_entity=legal_entity)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

