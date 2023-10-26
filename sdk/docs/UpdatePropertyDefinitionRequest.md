# UpdatePropertyDefinitionRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | The display name of the property. | 
**property_description** | **str** | Describes the property | [optional] 

## Example

```python
from lusid.models.update_property_definition_request import UpdatePropertyDefinitionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdatePropertyDefinitionRequest from a JSON string
update_property_definition_request_instance = UpdatePropertyDefinitionRequest.from_json(json)
# print the JSON string representation of the object
print UpdatePropertyDefinitionRequest.to_json()

# convert the object into a dict
update_property_definition_request_dict = update_property_definition_request_instance.to_dict()
# create an instance of UpdatePropertyDefinitionRequest from a dict
update_property_definition_request_form_dict = update_property_definition_request.from_dict(update_property_definition_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


