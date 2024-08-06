# ResourceListOfAccessControlledResource


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | [**List[AccessControlledResource]**](AccessControlledResource.md) |  | 
**href** | **str** |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
**next_page** | **str** |  | [optional] 
**previous_page** | **str** |  | [optional] 

## Example

```python
from lusid.models.resource_list_of_access_controlled_resource import ResourceListOfAccessControlledResource

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceListOfAccessControlledResource from a JSON string
resource_list_of_access_controlled_resource_instance = ResourceListOfAccessControlledResource.from_json(json)
# print the JSON string representation of the object
print ResourceListOfAccessControlledResource.to_json()

# convert the object into a dict
resource_list_of_access_controlled_resource_dict = resource_list_of_access_controlled_resource_instance.to_dict()
# create an instance of ResourceListOfAccessControlledResource from a dict
resource_list_of_access_controlled_resource_form_dict = resource_list_of_access_controlled_resource.from_dict(resource_list_of_access_controlled_resource_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


