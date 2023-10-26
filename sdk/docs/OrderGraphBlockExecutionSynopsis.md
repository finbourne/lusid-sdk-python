# OrderGraphBlockExecutionSynopsis


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quantity** | **float** | Total number of units executed. | 
**details** | [**List[OrderGraphBlockExecutionDetail]**](OrderGraphBlockExecutionDetail.md) | Identifiers for each execution in this block. | 

## Example

```python
from lusid.models.order_graph_block_execution_synopsis import OrderGraphBlockExecutionSynopsis

# TODO update the JSON string below
json = "{}"
# create an instance of OrderGraphBlockExecutionSynopsis from a JSON string
order_graph_block_execution_synopsis_instance = OrderGraphBlockExecutionSynopsis.from_json(json)
# print the JSON string representation of the object
print OrderGraphBlockExecutionSynopsis.to_json()

# convert the object into a dict
order_graph_block_execution_synopsis_dict = order_graph_block_execution_synopsis_instance.to_dict()
# create an instance of OrderGraphBlockExecutionSynopsis from a dict
order_graph_block_execution_synopsis_form_dict = order_graph_block_execution_synopsis.from_dict(order_graph_block_execution_synopsis_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


