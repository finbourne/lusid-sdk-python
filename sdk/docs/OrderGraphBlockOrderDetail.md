# OrderGraphBlockOrderDetail


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ResourceId**](ResourceId.md) |  | 
**compliance_state** | **str** | The compliance state of this order. Possible values are &#39;Pending&#39;, &#39;Failed&#39;, &#39;Manually approved&#39; and &#39;Passed&#39;. | 

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
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


