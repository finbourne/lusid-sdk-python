# DeletedEntityResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**effective_from** | **datetime** | The effective datetime at which the deletion became valid. May be null in the case where multiple date times are applicable. | [optional] 
**as_at** | **datetime** | The asAt datetime at which the deletion was committed to LUSID. | 
**entity_type** | **str** | The type of the entity that the deleted response applies to. | [optional] 
**entity_unique_id** | **str** | The unique Id of the entity that the deleted response applies to. | [optional] 
**staged_modifications** | [**StagedModificationsInfo**](StagedModificationsInfo.md) |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.deleted_entity_response import DeletedEntityResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeletedEntityResponse from a JSON string
deleted_entity_response_instance = DeletedEntityResponse.from_json(json)
# print the JSON string representation of the object
print DeletedEntityResponse.to_json()

# convert the object into a dict
deleted_entity_response_dict = deleted_entity_response_instance.to_dict()
# create an instance of DeletedEntityResponse from a dict
deleted_entity_response_form_dict = deleted_entity_response.from_dict(deleted_entity_response_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


