# PagedResourceListOfGroupReconciliationComparisonRuleset


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next_page** | **str** |  | [optional] 
**previous_page** | **str** |  | [optional] 
**values** | [**List[GroupReconciliationComparisonRuleset]**](GroupReconciliationComparisonRuleset.md) |  | 
**href** | **str** |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.paged_resource_list_of_group_reconciliation_comparison_ruleset import PagedResourceListOfGroupReconciliationComparisonRuleset

# TODO update the JSON string below
json = "{}"
# create an instance of PagedResourceListOfGroupReconciliationComparisonRuleset from a JSON string
paged_resource_list_of_group_reconciliation_comparison_ruleset_instance = PagedResourceListOfGroupReconciliationComparisonRuleset.from_json(json)
# print the JSON string representation of the object
print PagedResourceListOfGroupReconciliationComparisonRuleset.to_json()

# convert the object into a dict
paged_resource_list_of_group_reconciliation_comparison_ruleset_dict = paged_resource_list_of_group_reconciliation_comparison_ruleset_instance.to_dict()
# create an instance of PagedResourceListOfGroupReconciliationComparisonRuleset from a dict
paged_resource_list_of_group_reconciliation_comparison_ruleset_form_dict = paged_resource_list_of_group_reconciliation_comparison_ruleset.from_dict(paged_resource_list_of_group_reconciliation_comparison_ruleset_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


