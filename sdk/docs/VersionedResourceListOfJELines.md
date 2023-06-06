# VersionedResourceListOfJELines


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | [**Version**](Version.md) |  | 
**values** | [**List[JELines]**](JELines.md) |  | 
**href** | **str** |  | [optional] 
**next_page** | **str** |  | [optional] 
**previous_page** | **str** |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.versioned_resource_list_of_je_lines import VersionedResourceListOfJELines

# TODO update the JSON string below
json = "{}"
# create an instance of VersionedResourceListOfJELines from a JSON string
versioned_resource_list_of_je_lines_instance = VersionedResourceListOfJELines.from_json(json)
# print the JSON string representation of the object
print VersionedResourceListOfJELines.to_json()

# convert the object into a dict
versioned_resource_list_of_je_lines_dict = versioned_resource_list_of_je_lines_instance.to_dict()
# create an instance of VersionedResourceListOfJELines from a dict
versioned_resource_list_of_je_lines_form_dict = versioned_resource_list_of_je_lines.from_dict(versioned_resource_list_of_je_lines_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


