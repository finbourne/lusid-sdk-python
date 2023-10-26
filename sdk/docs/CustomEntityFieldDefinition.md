# CustomEntityFieldDefinition


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the field. | 
**lifetime** | **str** | Describes how the field’s values can change over time. The available values are: “Perpetual”, “TimeVariant”. | 
**type** | **str** | The value type for the field. Available values are: “String”, “Boolean”, “DateTime”, “Decimal”. | 
**collection_type** | **str** | The collection type for the field. Available values are: “Single”, “Array”. Null value defaults to “Single” | [optional] 
**required** | **bool** | Whether the field is required or not. | 
**description** | **str** | An optional description for the field. | [optional] 

## Example

```python
from lusid.models.custom_entity_field_definition import CustomEntityFieldDefinition

# TODO update the JSON string below
json = "{}"
# create an instance of CustomEntityFieldDefinition from a JSON string
custom_entity_field_definition_instance = CustomEntityFieldDefinition.from_json(json)
# print the JSON string representation of the object
print CustomEntityFieldDefinition.to_json()

# convert the object into a dict
custom_entity_field_definition_dict = custom_entity_field_definition_instance.to_dict()
# create an instance of CustomEntityFieldDefinition from a dict
custom_entity_field_definition_form_dict = custom_entity_field_definition.from_dict(custom_entity_field_definition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


