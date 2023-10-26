# ResourceId

Identifiers of an entity

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scope** | **str** | The scope used to identify an entity | 
**code** | **str** | The code used to identify an entity | 

## Example

```python
from lusid.models.resource_id import ResourceId

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceId from a JSON string
resource_id_instance = ResourceId.from_json(json)
# print the JSON string representation of the object
print ResourceId.to_json()

# convert the object into a dict
resource_id_dict = resource_id_instance.to_dict()
# create an instance of ResourceId from a dict
resource_id_form_dict = resource_id.from_dict(resource_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


