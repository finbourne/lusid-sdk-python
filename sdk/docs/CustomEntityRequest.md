# CustomEntityRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | A display label for the custom entity. | 
**description** | **str** | A description of the custom entity. | 
**identifiers** | [**List[CustomEntityId]**](CustomEntityId.md) | The identifiers the custom entity will be upserted with. | 
**fields** | [**List[CustomEntityField]**](CustomEntityField.md) | The fields that decorate the custom entity. | [optional] 
**properties** | [**Dict[str, ModelProperty]**](ModelProperty.md) | The properties that decorate the custom entity. | [optional] 
## Example

```python
from lusid.models.custom_entity_request import CustomEntityRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

display_name: StrictStr = "example_display_name"
description: StrictStr = "example_description"
identifiers: List[CustomEntityId] = # Replace with your value
fields: Optional[List[CustomEntityField]] = # Replace with your value
properties: Optional[Dict[str, ModelProperty]] = # Replace with your value
custom_entity_request_instance = CustomEntityRequest(display_name=display_name, description=description, identifiers=identifiers, fields=fields, properties=properties)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

