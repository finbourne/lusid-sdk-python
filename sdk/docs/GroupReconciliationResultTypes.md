# GroupReconciliationResultTypes


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count_match** | **int** | The number of comparison results of resultType \&quot;Match\&quot; with this instanceId and reconciliationType | 
**link_matches** | [**Link**](Link.md) |  | 
**count_partial_match** | **int** | The number of comparison results of resultType \&quot;PartialMatch\&quot; with this instanceId and reconciliationType | 
**link_partial_matches** | [**Link**](Link.md) |  | 
**count_break** | **int** | The number of comparison results of resultType \&quot;Break\&quot; with this instanceId and reconciliationType | 
**link_breaks** | [**Link**](Link.md) |  | 
**count_not_found** | **int** | The number of comparison results of resultType \&quot;Resolved\&quot; with this instanceId and reconciliationType | [optional] [readonly] 
**link_not_found** | [**Link**](Link.md) |  | [optional] 
**count_resolved** | **int** | The number of comparison results of resultType \&quot;Resolved\&quot; with this instanceId and reconciliationType | [optional] 
**link_resolved** | [**Link**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.group_reconciliation_result_types import GroupReconciliationResultTypes

# TODO update the JSON string below
json = "{}"
# create an instance of GroupReconciliationResultTypes from a JSON string
group_reconciliation_result_types_instance = GroupReconciliationResultTypes.from_json(json)
# print the JSON string representation of the object
print GroupReconciliationResultTypes.to_json()

# convert the object into a dict
group_reconciliation_result_types_dict = group_reconciliation_result_types_instance.to_dict()
# create an instance of GroupReconciliationResultTypes from a dict
group_reconciliation_result_types_form_dict = group_reconciliation_result_types.from_dict(group_reconciliation_result_types_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


