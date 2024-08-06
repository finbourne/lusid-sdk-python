# PagedResourceListOfPropertyDefinitionSearchResult


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next_page** | **str** |  | [optional] 
**previous_page** | **str** |  | [optional] 
**values** | [**List[PropertyDefinitionSearchResult]**](PropertyDefinitionSearchResult.md) |  | 
**href** | **str** |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.paged_resource_list_of_property_definition_search_result import PagedResourceListOfPropertyDefinitionSearchResult

# TODO update the JSON string below
json = "{}"
# create an instance of PagedResourceListOfPropertyDefinitionSearchResult from a JSON string
paged_resource_list_of_property_definition_search_result_instance = PagedResourceListOfPropertyDefinitionSearchResult.from_json(json)
# print the JSON string representation of the object
print PagedResourceListOfPropertyDefinitionSearchResult.to_json()

# convert the object into a dict
paged_resource_list_of_property_definition_search_result_dict = paged_resource_list_of_property_definition_search_result_instance.to_dict()
# create an instance of PagedResourceListOfPropertyDefinitionSearchResult from a dict
paged_resource_list_of_property_definition_search_result_form_dict = paged_resource_list_of_property_definition_search_result.from_dict(paged_resource_list_of_property_definition_search_result_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


