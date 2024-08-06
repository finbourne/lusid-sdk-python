# UpdateRelationshipDefinitionRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | The display name of the relation. | 
**outward_description** | **str** | The description to relate source entity object and target entity object. | 
**inward_description** | **str** | The description to relate target entity object and source entity object. | 

## Example

```python
from lusid.models.update_relationship_definition_request import UpdateRelationshipDefinitionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateRelationshipDefinitionRequest from a JSON string
update_relationship_definition_request_instance = UpdateRelationshipDefinitionRequest.from_json(json)
# print the JSON string representation of the object
print UpdateRelationshipDefinitionRequest.to_json()

# convert the object into a dict
update_relationship_definition_request_dict = update_relationship_definition_request_instance.to_dict()
# create an instance of UpdateRelationshipDefinitionRequest from a dict
update_relationship_definition_request_form_dict = update_relationship_definition_request.from_dict(update_relationship_definition_request_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


