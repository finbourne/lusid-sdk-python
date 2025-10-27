# OrderGraphBlockOrderDetail

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ResourceId**](ResourceId.md) |  | 
**compliance_state** | **str** | The compliance state of this order. Possible values are &#39;Pending&#39;, &#39;Failed&#39;, &#39;Manually approved&#39;, &#39;Passed&#39; and &#39;Warning&#39;. | 
**approval_state** | **str** | The approval state of this order. Possible values are &#39;Pending&#39;, &#39;Rejected&#39; and &#39;Approved&#39;. | 
**portfolio_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**portfolio_name** | **str** | The name of the order&#39;s referenced Portfolio. | [optional] 
**order_approval_task_id** | **str** | The task id associated with the approval state of the order. | [optional] 
**order_approval_task_definition_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**non_passing_compliance_rule_results** | [**List[ContributionToNonPassingRuleDetail]**](ContributionToNonPassingRuleDetail.md) | The details of compliance rules in non-passing states. | [optional] 
## Example

```python
from lusid.models.order_graph_block_order_detail import OrderGraphBlockOrderDetail
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

id: ResourceId
compliance_state: StrictStr = "example_compliance_state"
approval_state: StrictStr = "example_approval_state"
portfolio_id: Optional[ResourceId] = # Replace with your value
portfolio_name: Optional[StrictStr] = "example_portfolio_name"
order_approval_task_id: Optional[StrictStr] = "example_order_approval_task_id"
order_approval_task_definition_id: Optional[ResourceId] = # Replace with your value
non_passing_compliance_rule_results: Optional[List[ContributionToNonPassingRuleDetail]] = # Replace with your value
order_graph_block_order_detail_instance = OrderGraphBlockOrderDetail(id=id, compliance_state=compliance_state, approval_state=approval_state, portfolio_id=portfolio_id, portfolio_name=portfolio_name, order_approval_task_id=order_approval_task_id, order_approval_task_definition_id=order_approval_task_definition_id, non_passing_compliance_rule_results=non_passing_compliance_rule_results)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

