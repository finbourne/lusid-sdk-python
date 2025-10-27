# SetPersonIdentifiersRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifiers** | [**Dict[str, ModelProperty]**](ModelProperty.md) | Identifiers to set for a Person. Identifiers not included in the request will not be amended. | [optional] 
## Example

```python
from lusid.models.set_person_identifiers_request import SetPersonIdentifiersRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

identifiers: Optional[Dict[str, ModelProperty]] = # Replace with your value
set_person_identifiers_request_instance = SetPersonIdentifiersRequest(identifiers=identifiers)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

