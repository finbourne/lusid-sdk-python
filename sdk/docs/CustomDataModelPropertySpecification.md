# CustomDataModelPropertySpecification


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**property_key** | **str** | The property key that is required/allowed on the bound entity. | 
**required** | **bool** | Whether property is required or allowed. | [optional] 

## Example

```python
from lusid.models.custom_data_model_property_specification import CustomDataModelPropertySpecification

# TODO update the JSON string below
json = "{}"
# create an instance of CustomDataModelPropertySpecification from a JSON string
custom_data_model_property_specification_instance = CustomDataModelPropertySpecification.from_json(json)
# print the JSON string representation of the object
print CustomDataModelPropertySpecification.to_json()

# convert the object into a dict
custom_data_model_property_specification_dict = custom_data_model_property_specification_instance.to_dict()
# create an instance of CustomDataModelPropertySpecification from a dict
custom_data_model_property_specification_form_dict = custom_data_model_property_specification.from_dict(custom_data_model_property_specification_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


