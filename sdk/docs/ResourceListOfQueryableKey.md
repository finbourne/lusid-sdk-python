# ResourceListOfQueryableKey


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | [**List[QueryableKey]**](QueryableKey.md) |  | 
**href** | **str** |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
**next_page** | **str** |  | [optional] 
**previous_page** | **str** |  | [optional] 

## Example

```python
from lusid.models.resource_list_of_queryable_key import ResourceListOfQueryableKey

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceListOfQueryableKey from a JSON string
resource_list_of_queryable_key_instance = ResourceListOfQueryableKey.from_json(json)
# print the JSON string representation of the object
print ResourceListOfQueryableKey.to_json()

# convert the object into a dict
resource_list_of_queryable_key_dict = resource_list_of_queryable_key_instance.to_dict()
# create an instance of ResourceListOfQueryableKey from a dict
resource_list_of_queryable_key_form_dict = resource_list_of_queryable_key.from_dict(resource_list_of_queryable_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


