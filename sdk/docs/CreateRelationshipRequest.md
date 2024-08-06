# CreateRelationshipRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_entity_id** | **Dict[str, str]** | The identifier of the source entity. | 
**target_entity_id** | **Dict[str, str]** | The identifier of the target entity. | 
**effective_from** | **str** | The effective date of the relationship to be created | [optional] 
**effective_until** | **str** | The effective datetime until which the relationship is valid. If not supplied this will be valid indefinitely. | [optional] 

## Example

```python
from lusid.models.create_relationship_request import CreateRelationshipRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateRelationshipRequest from a JSON string
create_relationship_request_instance = CreateRelationshipRequest.from_json(json)
# print the JSON string representation of the object
print CreateRelationshipRequest.to_json()

# convert the object into a dict
create_relationship_request_dict = create_relationship_request_instance.to_dict()
# create an instance of CreateRelationshipRequest from a dict
create_relationship_request_form_dict = create_relationship_request.from_dict(create_relationship_request_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


