# InstrumentIdTypeDescriptor

The description of an allowable instrument identifier.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier_type** | **str** | The name of the identifier type. | 
**property_key** | **str** | The property key that corresponds to the identifier type. | 
**is_unique_identifier_type** | **bool** | Whether or not the identifier type is enforced to be unique. | 
## Example

```python
from lusid.models.instrument_id_type_descriptor import InstrumentIdTypeDescriptor
from typing import Any, Dict
from pydantic.v1 import BaseModel, Field, StrictBool, StrictStr, constr

identifier_type: StrictStr = "example_identifier_type"
property_key: StrictStr = "example_property_key"
is_unique_identifier_type: StrictBool = # Replace with your value
is_unique_identifier_type:StrictBool = True
instrument_id_type_descriptor_instance = InstrumentIdTypeDescriptor(identifier_type=identifier_type, property_key=property_key, is_unique_identifier_type=is_unique_identifier_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

