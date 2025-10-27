# SidesDefinitionRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**side** | **str** | A unique label identifying the side definition. | 
**side_request** | [**SideDefinitionRequest**](SideDefinitionRequest.md) |  | 
## Example

```python
from lusid.models.sides_definition_request import SidesDefinitionRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

side: StrictStr = "example_side"
side_request: SideDefinitionRequest = # Replace with your value
sides_definition_request_instance = SidesDefinitionRequest(side=side, side_request=side_request)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

