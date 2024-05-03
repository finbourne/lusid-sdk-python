# PagedResourceListOfStagedModificationsRequestedChangeInterval


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next_page** | **str** |  | [optional] 
**previous_page** | **str** |  | [optional] 
**values** | [**List[StagedModificationsRequestedChangeInterval]**](StagedModificationsRequestedChangeInterval.md) |  | 
**href** | **str** |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.paged_resource_list_of_staged_modifications_requested_change_interval import PagedResourceListOfStagedModificationsRequestedChangeInterval

# TODO update the JSON string below
json = "{}"
# create an instance of PagedResourceListOfStagedModificationsRequestedChangeInterval from a JSON string
paged_resource_list_of_staged_modifications_requested_change_interval_instance = PagedResourceListOfStagedModificationsRequestedChangeInterval.from_json(json)
# print the JSON string representation of the object
print PagedResourceListOfStagedModificationsRequestedChangeInterval.to_json()

# convert the object into a dict
paged_resource_list_of_staged_modifications_requested_change_interval_dict = paged_resource_list_of_staged_modifications_requested_change_interval_instance.to_dict()
# create an instance of PagedResourceListOfStagedModificationsRequestedChangeInterval from a dict
paged_resource_list_of_staged_modifications_requested_change_interval_form_dict = paged_resource_list_of_staged_modifications_requested_change_interval.from_dict(paged_resource_list_of_staged_modifications_requested_change_interval_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


