# ReconciliationRunBreak


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ReconciliationBreakId**](ReconciliationBreakId.md) |  | [optional] 
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**left_fields** | **Dict[str, str]** | Fields for the left hand side of the reconciliation | [optional] 
**right_fields** | **Dict[str, str]** | Fields for the right hand side of the reconciliation | [optional] 
**diff** | **str** | The difference between two matching fields | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.reconciliation_run_break import ReconciliationRunBreak

# TODO update the JSON string below
json = "{}"
# create an instance of ReconciliationRunBreak from a JSON string
reconciliation_run_break_instance = ReconciliationRunBreak.from_json(json)
# print the JSON string representation of the object
print ReconciliationRunBreak.to_json()

# convert the object into a dict
reconciliation_run_break_dict = reconciliation_run_break_instance.to_dict()
# create an instance of ReconciliationRunBreak from a dict
reconciliation_run_break_form_dict = reconciliation_run_break.from_dict(reconciliation_run_break_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


