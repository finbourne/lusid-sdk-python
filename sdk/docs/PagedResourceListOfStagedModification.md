# PagedResourceListOfStagedModification


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next_page** | **str** |  | [optional] 
**previous_page** | **str** |  | [optional] 
**values** | [**List[StagedModification]**](StagedModification.md) |  | 
**href** | **str** |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.paged_resource_list_of_staged_modification import PagedResourceListOfStagedModification

# TODO update the JSON string below
json = "{}"
# create an instance of PagedResourceListOfStagedModification from a JSON string
paged_resource_list_of_staged_modification_instance = PagedResourceListOfStagedModification.from_json(json)
# print the JSON string representation of the object
print PagedResourceListOfStagedModification.to_json()

# convert the object into a dict
paged_resource_list_of_staged_modification_dict = paged_resource_list_of_staged_modification_instance.to_dict()
# create an instance of PagedResourceListOfStagedModification from a dict
paged_resource_list_of_staged_modification_form_dict = paged_resource_list_of_staged_modification.from_dict(paged_resource_list_of_staged_modification_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


