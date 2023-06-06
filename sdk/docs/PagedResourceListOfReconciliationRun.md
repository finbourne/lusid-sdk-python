# PagedResourceListOfReconciliationRun


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next_page** | **str** |  | [optional] 
**previous_page** | **str** |  | [optional] 
**values** | [**List[ReconciliationRun]**](ReconciliationRun.md) |  | 
**href** | **str** |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.paged_resource_list_of_reconciliation_run import PagedResourceListOfReconciliationRun

# TODO update the JSON string below
json = "{}"
# create an instance of PagedResourceListOfReconciliationRun from a JSON string
paged_resource_list_of_reconciliation_run_instance = PagedResourceListOfReconciliationRun.from_json(json)
# print the JSON string representation of the object
print PagedResourceListOfReconciliationRun.to_json()

# convert the object into a dict
paged_resource_list_of_reconciliation_run_dict = paged_resource_list_of_reconciliation_run_instance.to_dict()
# create an instance of PagedResourceListOfReconciliationRun from a dict
paged_resource_list_of_reconciliation_run_form_dict = paged_resource_list_of_reconciliation_run.from_dict(paged_resource_list_of_reconciliation_run_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


