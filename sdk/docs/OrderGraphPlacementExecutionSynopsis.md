# OrderGraphPlacementExecutionSynopsis


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quantity** | **float** | Total number of units executed. | 
**details** | [**List[OrderGraphPlacementExecutionDetail]**](OrderGraphPlacementExecutionDetail.md) | Identifiers info for each execution against this placement. | 

## Example

```python
from lusid.models.order_graph_placement_execution_synopsis import OrderGraphPlacementExecutionSynopsis

# TODO update the JSON string below
json = "{}"
# create an instance of OrderGraphPlacementExecutionSynopsis from a JSON string
order_graph_placement_execution_synopsis_instance = OrderGraphPlacementExecutionSynopsis.from_json(json)
# print the JSON string representation of the object
print OrderGraphPlacementExecutionSynopsis.to_json()

# convert the object into a dict
order_graph_placement_execution_synopsis_dict = order_graph_placement_execution_synopsis_instance.to_dict()
# create an instance of OrderGraphPlacementExecutionSynopsis from a dict
order_graph_placement_execution_synopsis_form_dict = order_graph_placement_execution_synopsis.from_dict(order_graph_placement_execution_synopsis_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


