# ResourceListOfRelation


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | [**List[Relation]**](Relation.md) |  | 
**href** | **str** |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
**next_page** | **str** |  | [optional] 
**previous_page** | **str** |  | [optional] 

## Example

```python
from lusid.models.resource_list_of_relation import ResourceListOfRelation

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceListOfRelation from a JSON string
resource_list_of_relation_instance = ResourceListOfRelation.from_json(json)
# print the JSON string representation of the object
print ResourceListOfRelation.to_json()

# convert the object into a dict
resource_list_of_relation_dict = resource_list_of_relation_instance.to_dict()
# create an instance of ResourceListOfRelation from a dict
resource_list_of_relation_form_dict = resource_list_of_relation.from_dict(resource_list_of_relation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


