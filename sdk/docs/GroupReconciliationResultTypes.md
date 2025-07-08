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
**count_resolved** | **int** | The number of comparison results of resultType \&quot;Resolved\&quot; with this instanceId and reconciliationType | 
**link_resolved** | [**Link**](Link.md) |  | 
## Example

```python
from lusid.models.group_reconciliation_result_types import GroupReconciliationResultTypes
from typing import Any, Dict
from pydantic.v1 import BaseModel, Field, StrictInt

count_match: StrictInt = # Replace with your value
count_match: StrictInt = 42
link_matches: Link = # Replace with your value
count_partial_match: StrictInt = # Replace with your value
count_partial_match: StrictInt = 42
link_partial_matches: Link = # Replace with your value
count_break: StrictInt = # Replace with your value
count_break: StrictInt = 42
link_breaks: Link = # Replace with your value
count_resolved: StrictInt = # Replace with your value
count_resolved: StrictInt = 42
link_resolved: Link = # Replace with your value
group_reconciliation_result_types_instance = GroupReconciliationResultTypes(count_match=count_match, link_matches=link_matches, count_partial_match=count_partial_match, link_partial_matches=link_partial_matches, count_break=count_break, link_breaks=link_breaks, count_resolved=count_resolved, link_resolved=link_resolved)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

