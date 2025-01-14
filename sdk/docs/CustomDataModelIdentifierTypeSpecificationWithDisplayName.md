# CustomDataModelIdentifierTypeSpecificationWithDisplayName


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | The display name of the property definition. | [optional] 
**identifier_key** | **str** | The identifier type that is required/allowed on the bound entity. | 
**required** | **bool** | Whether dentifier type is required or allowed. | [optional] 

## Example

```python
from lusid.models.custom_data_model_identifier_type_specification_with_display_name import CustomDataModelIdentifierTypeSpecificationWithDisplayName

# TODO update the JSON string below
json = "{}"
# create an instance of CustomDataModelIdentifierTypeSpecificationWithDisplayName from a JSON string
custom_data_model_identifier_type_specification_with_display_name_instance = CustomDataModelIdentifierTypeSpecificationWithDisplayName.from_json(json)
# print the JSON string representation of the object
print CustomDataModelIdentifierTypeSpecificationWithDisplayName.to_json()

# convert the object into a dict
custom_data_model_identifier_type_specification_with_display_name_dict = custom_data_model_identifier_type_specification_with_display_name_instance.to_dict()
# create an instance of CustomDataModelIdentifierTypeSpecificationWithDisplayName from a dict
custom_data_model_identifier_type_specification_with_display_name_form_dict = custom_data_model_identifier_type_specification_with_display_name.from_dict(custom_data_model_identifier_type_specification_with_display_name_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


