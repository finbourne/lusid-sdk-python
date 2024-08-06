# UpdateDerivedPropertyDefinitionRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | The display name of the property. | 
**data_type_id** | [**ResourceId**](ResourceId.md) |  | 
**property_description** | **str** | Describes the property | [optional] 
**derivation_formula** | **str** | The rule that defines how data is composed for a derived property. | 

## Example

```python
from lusid.models.update_derived_property_definition_request import UpdateDerivedPropertyDefinitionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateDerivedPropertyDefinitionRequest from a JSON string
update_derived_property_definition_request_instance = UpdateDerivedPropertyDefinitionRequest.from_json(json)
# print the JSON string representation of the object
print UpdateDerivedPropertyDefinitionRequest.to_json()

# convert the object into a dict
update_derived_property_definition_request_dict = update_derived_property_definition_request_instance.to_dict()
# create an instance of UpdateDerivedPropertyDefinitionRequest from a dict
update_derived_property_definition_request_form_dict = update_derived_property_definition_request.from_dict(update_derived_property_definition_request_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


