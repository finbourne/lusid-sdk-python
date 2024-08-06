# UpsertCustomEntitiesResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**values** | [**Dict[str, CustomEntityResponse]**](CustomEntityResponse.md) | The custom-entities which have been successfully updated or created. | [optional] 
**failed** | [**Dict[str, ErrorDetail]**](ErrorDetail.md) | The custom-entities that could not be updated or created or were left unchanged without error along with a reason for their failure. | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.upsert_custom_entities_response import UpsertCustomEntitiesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpsertCustomEntitiesResponse from a JSON string
upsert_custom_entities_response_instance = UpsertCustomEntitiesResponse.from_json(json)
# print the JSON string representation of the object
print UpsertCustomEntitiesResponse.to_json()

# convert the object into a dict
upsert_custom_entities_response_dict = upsert_custom_entities_response_instance.to_dict()
# create an instance of UpsertCustomEntitiesResponse from a dict
upsert_custom_entities_response_form_dict = upsert_custom_entities_response.from_dict(upsert_custom_entities_response_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


