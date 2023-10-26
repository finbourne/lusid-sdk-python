# ReconciliationRunId


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reconciliation** | [**ReconciliationId**](ReconciliationId.md) |  | [optional] 
**var_date** | **datetime** |  | [optional] 
**version** | **int** |  | [optional] 
**as_string** | **str** |  | [optional] [readonly] 

## Example

```python
from lusid.models.reconciliation_run_id import ReconciliationRunId

# TODO update the JSON string below
json = "{}"
# create an instance of ReconciliationRunId from a JSON string
reconciliation_run_id_instance = ReconciliationRunId.from_json(json)
# print the JSON string representation of the object
print ReconciliationRunId.to_json()

# convert the object into a dict
reconciliation_run_id_dict = reconciliation_run_id_instance.to_dict()
# create an instance of ReconciliationRunId from a dict
reconciliation_run_id_form_dict = reconciliation_run_id.from_dict(reconciliation_run_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


