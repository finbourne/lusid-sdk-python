# PagedResourceListOfPostingModuleRule


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next_page** | **str** |  | [optional] 
**previous_page** | **str** |  | [optional] 
**values** | [**List[PostingModuleRule]**](PostingModuleRule.md) |  | 
**href** | **str** |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.paged_resource_list_of_posting_module_rule import PagedResourceListOfPostingModuleRule

# TODO update the JSON string below
json = "{}"
# create an instance of PagedResourceListOfPostingModuleRule from a JSON string
paged_resource_list_of_posting_module_rule_instance = PagedResourceListOfPostingModuleRule.from_json(json)
# print the JSON string representation of the object
print PagedResourceListOfPostingModuleRule.to_json()

# convert the object into a dict
paged_resource_list_of_posting_module_rule_dict = paged_resource_list_of_posting_module_rule_instance.to_dict()
# create an instance of PagedResourceListOfPostingModuleRule from a dict
paged_resource_list_of_posting_module_rule_form_dict = paged_resource_list_of_posting_module_rule.from_dict(paged_resource_list_of_posting_module_rule_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


