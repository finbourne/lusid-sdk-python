# DeleteRelationRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_entity_id** | **Dict[str, str]** | The identifier of the source entity of the relation to be deleted. | 
**target_entity_id** | **Dict[str, str]** | The identifier of the target entity of the relation to be deleted. | 

## Example

```python
from lusid.models.delete_relation_request import DeleteRelationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteRelationRequest from a JSON string
delete_relation_request_instance = DeleteRelationRequest.from_json(json)
# print the JSON string representation of the object
print DeleteRelationRequest.to_json()

# convert the object into a dict
delete_relation_request_dict = delete_relation_request_instance.to_dict()
# create an instance of DeleteRelationRequest from a dict
delete_relation_request_form_dict = delete_relation_request.from_dict(delete_relation_request_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


