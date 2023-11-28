# PagedResourceListOfCleardownModuleRule


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next_page** | **str** |  | [optional] 
**previous_page** | **str** |  | [optional] 
**values** | [**List[CleardownModuleRule]**](CleardownModuleRule.md) |  | 
**href** | **str** |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.paged_resource_list_of_cleardown_module_rule import PagedResourceListOfCleardownModuleRule

# TODO update the JSON string below
json = "{}"
# create an instance of PagedResourceListOfCleardownModuleRule from a JSON string
paged_resource_list_of_cleardown_module_rule_instance = PagedResourceListOfCleardownModuleRule.from_json(json)
# print the JSON string representation of the object
print PagedResourceListOfCleardownModuleRule.to_json()

# convert the object into a dict
paged_resource_list_of_cleardown_module_rule_dict = paged_resource_list_of_cleardown_module_rule_instance.to_dict()
# create an instance of PagedResourceListOfCleardownModuleRule from a dict
paged_resource_list_of_cleardown_module_rule_form_dict = paged_resource_list_of_cleardown_module_rule.from_dict(paged_resource_list_of_cleardown_module_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


