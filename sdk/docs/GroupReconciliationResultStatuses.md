# GroupReconciliationResultStatuses

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count_new** | **int** | The number of comparison results of resultStatus \&quot;New\&quot; with this instanceId and reconciliationType | 
**link_new** | [**Link**](Link.md) |  | 
**count_confirmed** | **int** | The number of comparison results of resultStatus \&quot;Confirmed\&quot; with this instanceId and reconciliationType | 
**link_confirmed** | [**Link**](Link.md) |  | 
**count_changed** | **int** | The number of comparison results of resultStatus \&quot;Changed\&quot; with this instanceId and reconciliationType | 
**link_changed** | [**Link**](Link.md) |  | 
## Example

```python
from lusid.models.group_reconciliation_result_statuses import GroupReconciliationResultStatuses
from typing import Any, Dict
from pydantic.v1 import BaseModel, Field, StrictInt

count_new: StrictInt = # Replace with your value
count_new: StrictInt = 42
link_new: Link = # Replace with your value
count_confirmed: StrictInt = # Replace with your value
count_confirmed: StrictInt = 42
link_confirmed: Link = # Replace with your value
count_changed: StrictInt = # Replace with your value
count_changed: StrictInt = 42
link_changed: Link = # Replace with your value
group_reconciliation_result_statuses_instance = GroupReconciliationResultStatuses(count_new=count_new, link_new=link_new, count_confirmed=count_confirmed, link_confirmed=link_confirmed, count_changed=count_changed, link_changed=link_changed)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

