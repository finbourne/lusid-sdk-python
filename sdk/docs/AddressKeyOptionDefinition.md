# AddressKeyOptionDefinition

The definition of an Address Key Option
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the option | 
**type** | **str** | The type of the option | 
**description** | **str** | The description of the option | 
**optional** | **bool** | Is this option required or optional? | 
**allowed_value_set** | **List[str]** | If the option is a string or enum, the allowed set of values it can take. | [optional] 
**default_value** | **str** | If the option is not required, what is the default value? | [optional] 
## Example

```python
from lusid.models.address_key_option_definition import AddressKeyOptionDefinition
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictBool, StrictStr, conlist, constr

name: StrictStr = "example_name"
type: StrictStr = "example_type"
description: StrictStr = "example_description"
optional: StrictBool = # Replace with your value
optional:StrictBool = True
allowed_value_set: Optional[conlist(StrictStr)] = # Replace with your value
default_value: Optional[StrictStr] = "example_default_value"
address_key_option_definition_instance = AddressKeyOptionDefinition(name=name, type=type, description=description, optional=optional, allowed_value_set=allowed_value_set, default_value=default_value)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

