# DeleteRelationshipRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_entity_id** | **Dict[str, str]** | The identifier of the source entity of the relationship to be deleted. | 
**target_entity_id** | **Dict[str, str]** | The identifier of the target entity of the relationship to be deleted. | 
**effective_from** | **str** | The effective date of the relationship to be deleted | [optional] 
**effective_until** | **str** | The effective datetime until which the relationship will be deleted. If not supplied the deletion will be permanent. | [optional] 

## Example

```python
from lusid.models.delete_relationship_request import DeleteRelationshipRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteRelationshipRequest from a JSON string
delete_relationship_request_instance = DeleteRelationshipRequest.from_json(json)
# print the JSON string representation of the object
print DeleteRelationshipRequest.to_json()

# convert the object into a dict
delete_relationship_request_dict = delete_relationship_request_instance.to_dict()
# create an instance of DeleteRelationshipRequest from a dict
delete_relationship_request_form_dict = delete_relationship_request.from_dict(delete_relationship_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


