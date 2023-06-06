# ReconciliationBreakId


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reconciliation_run** | [**ReconciliationRunId**](ReconciliationRunId.md) |  | [optional] 
**break_id** | **str** |  | [optional] 
**as_string** | **str** |  | [optional] [readonly] 

## Example

```python
from lusid.models.reconciliation_break_id import ReconciliationBreakId

# TODO update the JSON string below
json = "{}"
# create an instance of ReconciliationBreakId from a JSON string
reconciliation_break_id_instance = ReconciliationBreakId.from_json(json)
# print the JSON string representation of the object
print ReconciliationBreakId.to_json()

# convert the object into a dict
reconciliation_break_id_dict = reconciliation_break_id_instance.to_dict()
# create an instance of ReconciliationBreakId from a dict
reconciliation_break_id_form_dict = reconciliation_break_id.from_dict(reconciliation_break_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


