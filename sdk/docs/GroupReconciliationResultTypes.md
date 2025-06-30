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
from typing import Any, Dict, Optional
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
count_not_found: Optional[StrictInt] = # Replace with your value
count_not_found: Optional[StrictInt] = None
link_not_found: Optional[Link] = # Replace with your value
count_resolved: Optional[StrictInt] = # Replace with your value
count_resolved: Optional[StrictInt] = None
link_resolved: Optional[Link] = # Replace with your value
group_reconciliation_result_types_instance = GroupReconciliationResultTypes(count_match=count_match, link_matches=link_matches, count_partial_match=count_partial_match, link_partial_matches=link_partial_matches, count_break=count_break, link_breaks=link_breaks, count_not_found=count_not_found, link_not_found=link_not_found, count_resolved=count_resolved, link_resolved=link_resolved)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

