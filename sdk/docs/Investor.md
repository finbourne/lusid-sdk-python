# Investor

Representation of an Investor on the LUSID API
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**investor_type** | **str** | The type of the Investor | [optional] 
**identifiers** | **Dict[str, Optional[str]]** | The identifiers of the Investor | [optional] 
**entity_unique_id** | **str** | The unique Investor entity identifier | [optional] 
**person** | [**Person**](Person.md) |  | [optional] 
**legal_entity** | [**LegalEntity**](LegalEntity.md) |  | [optional] 
## Example

```python
from lusid.models.investor import Investor
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

investor_type: Optional[StrictStr] = "example_investor_type"
identifiers: Optional[Dict[str, Optional[StrictStr]]] = # Replace with your value
entity_unique_id: Optional[StrictStr] = "example_entity_unique_id"
person: Optional[Person] = None
legal_entity: Optional[LegalEntity] = # Replace with your value
investor_instance = Investor(investor_type=investor_type, identifiers=identifiers, entity_unique_id=entity_unique_id, person=person, legal_entity=legal_entity)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

