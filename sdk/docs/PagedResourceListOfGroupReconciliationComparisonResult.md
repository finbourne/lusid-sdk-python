# PagedResourceListOfGroupReconciliationComparisonResult


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next_page** | **str** |  | [optional] 
**previous_page** | **str** |  | [optional] 
**values** | [**List[GroupReconciliationComparisonResult]**](GroupReconciliationComparisonResult.md) |  | 
**href** | **str** |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.paged_resource_list_of_group_reconciliation_comparison_result import PagedResourceListOfGroupReconciliationComparisonResult

# TODO update the JSON string below
json = "{}"
# create an instance of PagedResourceListOfGroupReconciliationComparisonResult from a JSON string
paged_resource_list_of_group_reconciliation_comparison_result_instance = PagedResourceListOfGroupReconciliationComparisonResult.from_json(json)
# print the JSON string representation of the object
print PagedResourceListOfGroupReconciliationComparisonResult.to_json()

# convert the object into a dict
paged_resource_list_of_group_reconciliation_comparison_result_dict = paged_resource_list_of_group_reconciliation_comparison_result_instance.to_dict()
# create an instance of PagedResourceListOfGroupReconciliationComparisonResult from a dict
paged_resource_list_of_group_reconciliation_comparison_result_form_dict = paged_resource_list_of_group_reconciliation_comparison_result.from_dict(paged_resource_list_of_group_reconciliation_comparison_result_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


