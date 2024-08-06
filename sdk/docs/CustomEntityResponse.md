# CustomEntityResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**entity_type** | **str** | The type of custom entity this is. | 
**version** | [**Version**](Version.md) |  | 
**display_name** | **str** | A display label for the custom entity. | 
**description** | **str** | A description of the custom entity. | [optional] 
**identifiers** | [**List[CustomEntityId]**](CustomEntityId.md) | The identifiers the custom entity will be upserted with. | 
**fields** | [**List[CustomEntityField]**](CustomEntityField.md) | The fields that decorate the custom entity. | 
**relationships** | [**List[Relationship]**](Relationship.md) | A set of relationships associated to the custom entity. | 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.custom_entity_response import CustomEntityResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CustomEntityResponse from a JSON string
custom_entity_response_instance = CustomEntityResponse.from_json(json)
# print the JSON string representation of the object
print CustomEntityResponse.to_json()

# convert the object into a dict
custom_entity_response_dict = custom_entity_response_instance.to_dict()
# create an instance of CustomEntityResponse from a dict
custom_entity_response_form_dict = custom_entity_response.from_dict(custom_entity_response_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


