# CreateAddressKeyDefinitionRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address_key** | **str** | The address key of the address key definition. | 
**type** | **str** | The type of the address key definition | 
## Example

```python
from lusid.models.create_address_key_definition_request import CreateAddressKeyDefinitionRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

address_key: StrictStr = "example_address_key"
type: StrictStr = "example_type"
create_address_key_definition_request_instance = CreateAddressKeyDefinitionRequest(address_key=address_key, type=type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

