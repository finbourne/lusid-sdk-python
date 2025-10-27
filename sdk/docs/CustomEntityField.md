# CustomEntityField

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the field in the custom entity type definition. | 
**value** | **object** | The value for the field. | [optional] 
**effective_from** | **datetime** | The effective datetime from which the field&#39;s value is valid. For timeVariant fields, this defaults to the beginning of time. | [optional] 
**effective_until** | **datetime** | The effective datetime until which the field&#39;s value is valid. If not supplied, the value will be valid indefinitely or until the next “effectiveFrom” date of the field. | [optional] 
## Example

```python
from lusid.models.custom_entity_field import CustomEntityField
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

name: StrictStr = "example_name"
value: Optional[Any] = # Replace with your value
effective_from: Optional[datetime] = # Replace with your value
effective_until: Optional[datetime] = # Replace with your value
custom_entity_field_instance = CustomEntityField(name=name, value=value, effective_from=effective_from, effective_until=effective_until)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

