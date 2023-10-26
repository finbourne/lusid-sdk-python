# CreateRelationRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_entity_id** | **Dict[str, str]** | The identifier of the source entity. | 
**target_entity_id** | **Dict[str, str]** | The identifier of the target entity. | 

## Example

```python
from lusid.models.create_relation_request import CreateRelationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateRelationRequest from a JSON string
create_relation_request_instance = CreateRelationRequest.from_json(json)
# print the JSON string representation of the object
print CreateRelationRequest.to_json()

# convert the object into a dict
create_relation_request_dict = create_relation_request_instance.to_dict()
# create an instance of CreateRelationRequest from a dict
create_relation_request_form_dict = create_relation_request.from_dict(create_relation_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


