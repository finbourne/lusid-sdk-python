# ReconciliationRun

Representation of a reconciliation run in LUSID Api

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ReconciliationRunId**](ReconciliationRunId.md) |  | [optional] 
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.reconciliation_run import ReconciliationRun

# TODO update the JSON string below
json = "{}"
# create an instance of ReconciliationRun from a JSON string
reconciliation_run_instance = ReconciliationRun.from_json(json)
# print the JSON string representation of the object
print ReconciliationRun.to_json()

# convert the object into a dict
reconciliation_run_dict = reconciliation_run_instance.to_dict()
# create an instance of ReconciliationRun from a dict
reconciliation_run_form_dict = reconciliation_run.from_dict(reconciliation_run_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


