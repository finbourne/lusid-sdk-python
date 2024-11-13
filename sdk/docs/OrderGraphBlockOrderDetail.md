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

# TODO update the JSON string below
json = "{}"
# create an instance of OrderGraphBlockOrderDetail from a JSON string
order_graph_block_order_detail_instance = OrderGraphBlockOrderDetail.from_json(json)
# print the JSON string representation of the object
print OrderGraphBlockOrderDetail.to_json()

# convert the object into a dict
order_graph_block_order_detail_dict = order_graph_block_order_detail_instance.to_dict()
# create an instance of OrderGraphBlockOrderDetail from a dict
order_graph_block_order_detail_form_dict = order_graph_block_order_detail.from_dict(order_graph_block_order_detail_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


