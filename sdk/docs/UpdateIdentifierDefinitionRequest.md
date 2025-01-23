# UpdateIdentifierDefinitionRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hierarchy_level** | **str** | Optional metadata associated with the identifier definition. | [optional] 
**display_name** | **str** | A display name for the identifier. E.g. Figi. | [optional] 
**description** | **str** | An optional description for the identifier. | [optional] 
**properties** | [**Dict[str, ModelProperty]**](ModelProperty.md) | A set of properties for the identifier definition. | [optional] 

## Example

```python
from lusid.models.update_identifier_definition_request import UpdateIdentifierDefinitionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateIdentifierDefinitionRequest from a JSON string
update_identifier_definition_request_instance = UpdateIdentifierDefinitionRequest.from_json(json)
# print the JSON string representation of the object
print UpdateIdentifierDefinitionRequest.to_json()

# convert the object into a dict
update_identifier_definition_request_dict = update_identifier_definition_request_instance.to_dict()
# create an instance of UpdateIdentifierDefinitionRequest from a dict
update_identifier_definition_request_form_dict = update_identifier_definition_request.from_dict(update_identifier_definition_request_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


