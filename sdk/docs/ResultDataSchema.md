# ResultDataSchema

The shape and type of the returned data. The AddressSchema gives information about the requested keys,  including the return type, links to further documentation, lifecycle status and removal date if they are  deprecated.                Note: the NodeValueSchema and PropertySchema fields have been deprecated. Please use the AddressSchema instead.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node_value_schema** | [**Dict[str, FieldSchema]**](FieldSchema.md) | This has been deprecated. Please use AddressSchema instead. | [optional] 
**property_schema** | [**Dict[str, FieldSchema]**](FieldSchema.md) | This has been deprecated. Please use AddressSchema instead. | [optional] 
**address_schema** | [**Dict[str, AddressDefinition]**](AddressDefinition.md) |  | [optional] 

## Example

```python
from lusid.models.result_data_schema import ResultDataSchema

# TODO update the JSON string below
json = "{}"
# create an instance of ResultDataSchema from a JSON string
result_data_schema_instance = ResultDataSchema.from_json(json)
# print the JSON string representation of the object
print ResultDataSchema.to_json()

# convert the object into a dict
result_data_schema_dict = result_data_schema_instance.to_dict()
# create an instance of ResultDataSchema from a dict
result_data_schema_form_dict = result_data_schema.from_dict(result_data_schema_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


