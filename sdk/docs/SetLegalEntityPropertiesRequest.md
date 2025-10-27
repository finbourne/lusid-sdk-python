# SetLegalEntityPropertiesRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**properties** | [**Dict[str, ModelProperty]**](ModelProperty.md) | Properties to set for a Legal Entity. All time-variant properties must have same EffectiveFrom date. Properties not included in the request will not be amended. | [optional] 
## Example

```python
from lusid.models.set_legal_entity_properties_request import SetLegalEntityPropertiesRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

properties: Optional[Dict[str, ModelProperty]] = # Replace with your value
set_legal_entity_properties_request_instance = SetLegalEntityPropertiesRequest(properties=properties)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

