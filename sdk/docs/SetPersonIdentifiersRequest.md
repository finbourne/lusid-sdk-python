# SetPersonIdentifiersRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifiers** | [**Dict[str, ModelProperty]**](ModelProperty.md) | Identifiers to set for a Person. Identifiers not included in the request will not be amended. | [optional] 
## Example

```python
from lusid.models.set_person_identifiers_request import SetPersonIdentifiersRequest
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field

identifiers: Optional[Dict[str, ModelProperty]] = # Replace with your value
set_person_identifiers_request_instance = SetPersonIdentifiersRequest(identifiers=identifiers)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

