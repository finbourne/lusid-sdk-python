# ResourceListOfAccessMetadataValueOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | **List[List[AccessMetadataValue]]** |  | 
**href** | **str** |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
**next_page** | **str** |  | [optional] 
**previous_page** | **str** |  | [optional] 

## Example

```python
from lusid.models.resource_list_of_access_metadata_value_of import ResourceListOfAccessMetadataValueOf

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceListOfAccessMetadataValueOf from a JSON string
resource_list_of_access_metadata_value_of_instance = ResourceListOfAccessMetadataValueOf.from_json(json)
# print the JSON string representation of the object
print ResourceListOfAccessMetadataValueOf.to_json()

# convert the object into a dict
resource_list_of_access_metadata_value_of_dict = resource_list_of_access_metadata_value_of_instance.to_dict()
# create an instance of ResourceListOfAccessMetadataValueOf from a dict
resource_list_of_access_metadata_value_of_form_dict = resource_list_of_access_metadata_value_of.from_dict(resource_list_of_access_metadata_value_of_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


