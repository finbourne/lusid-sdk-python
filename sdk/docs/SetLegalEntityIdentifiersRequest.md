# SetLegalEntityIdentifiersRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifiers** | [**Dict[str, ModelProperty]**](ModelProperty.md) | Identifiers to set for a Legal Entity. Identifiers not included in the request will not be amended. | [optional] 
## Example

```python
from lusid.models.set_legal_entity_identifiers_request import SetLegalEntityIdentifiersRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

identifiers: Optional[Dict[str, ModelProperty]] = # Replace with your value
set_legal_entity_identifiers_request_instance = SetLegalEntityIdentifiersRequest(identifiers=identifiers)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

