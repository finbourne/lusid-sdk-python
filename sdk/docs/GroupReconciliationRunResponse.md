# GroupReconciliationRunResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reconciliation_summaries** | [**List[GroupReconciliationSummary]**](GroupReconciliationSummary.md) | One summary record for each of the \&quot;Holding\&quot; | \&quot;Transaction\&quot; | \&quot;Valuation\&quot; reconciliations performed | 

## Example

```python
from lusid.models.group_reconciliation_run_response import GroupReconciliationRunResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GroupReconciliationRunResponse from a JSON string
group_reconciliation_run_response_instance = GroupReconciliationRunResponse.from_json(json)
# print the JSON string representation of the object
print GroupReconciliationRunResponse.to_json()

# convert the object into a dict
group_reconciliation_run_response_dict = group_reconciliation_run_response_instance.to_dict()
# create an instance of GroupReconciliationRunResponse from a dict
group_reconciliation_run_response_form_dict = group_reconciliation_run_response.from_dict(group_reconciliation_run_response_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


