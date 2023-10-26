# PagedResourceListOfCorporateActionSource


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next_page** | **str** |  | [optional] 
**previous_page** | **str** |  | [optional] 
**values** | [**List[CorporateActionSource]**](CorporateActionSource.md) |  | 
**href** | **str** |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.paged_resource_list_of_corporate_action_source import PagedResourceListOfCorporateActionSource

# TODO update the JSON string below
json = "{}"
# create an instance of PagedResourceListOfCorporateActionSource from a JSON string
paged_resource_list_of_corporate_action_source_instance = PagedResourceListOfCorporateActionSource.from_json(json)
# print the JSON string representation of the object
print PagedResourceListOfCorporateActionSource.to_json()

# convert the object into a dict
paged_resource_list_of_corporate_action_source_dict = paged_resource_list_of_corporate_action_source_instance.to_dict()
# create an instance of PagedResourceListOfCorporateActionSource from a dict
paged_resource_list_of_corporate_action_source_form_dict = paged_resource_list_of_corporate_action_source.from_dict(paged_resource_list_of_corporate_action_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


