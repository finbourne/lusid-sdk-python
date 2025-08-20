# ResultDataSchema

The shape and type of the returned data. The AddressSchema gives information about the requested keys, including the return type, links to further documentation, lifecycle status and removal date if they are deprecated.              Note: the NodeValueSchema and PropertySchema fields have been deprecated. Please use the AddressSchema instead.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node_value_schema** | [**Dict[str, FieldSchema]**](FieldSchema.md) | This has been deprecated. Please use AddressSchema instead. | [optional] 
**property_schema** | [**Dict[str, FieldSchema]**](FieldSchema.md) | This has been deprecated. Please use AddressSchema instead. | [optional] 
**address_schema** | [**Dict[str, AddressDefinition]**](AddressDefinition.md) |  | [optional] 
## Example

```python
from lusid.models.result_data_schema import ResultDataSchema
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field

node_value_schema: Optional[Dict[str, FieldSchema]] = # Replace with your value
property_schema: Optional[Dict[str, FieldSchema]] = # Replace with your value
address_schema: Optional[Dict[str, AddressDefinition]] = # Replace with your value
result_data_schema_instance = ResultDataSchema(node_value_schema=node_value_schema, property_schema=property_schema, address_schema=address_schema)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

