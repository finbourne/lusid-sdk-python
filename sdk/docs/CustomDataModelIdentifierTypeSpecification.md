# CustomDataModelIdentifierTypeSpecification


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier_key** | **str** | The identifier type that is required/allowed on the bound entity. | 
**required** | **bool** | Whether dentifier type is required or allowed. | [optional] 

## Example

```python
from lusid.models.custom_data_model_identifier_type_specification import CustomDataModelIdentifierTypeSpecification

# TODO update the JSON string below
json = "{}"
# create an instance of CustomDataModelIdentifierTypeSpecification from a JSON string
custom_data_model_identifier_type_specification_instance = CustomDataModelIdentifierTypeSpecification.from_json(json)
# print the JSON string representation of the object
print CustomDataModelIdentifierTypeSpecification.to_json()

# convert the object into a dict
custom_data_model_identifier_type_specification_dict = custom_data_model_identifier_type_specification_instance.to_dict()
# create an instance of CustomDataModelIdentifierTypeSpecification from a dict
custom_data_model_identifier_type_specification_form_dict = custom_data_model_identifier_type_specification.from_dict(custom_data_model_identifier_type_specification_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


