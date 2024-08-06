# OrderGraphBlockTransactionSynopsis


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quantity** | **float** | Total number of units booked. | 
**details** | [**List[OrderGraphBlockTransactionDetail]**](OrderGraphBlockTransactionDetail.md) | Identifiers for each transaction in this block. | 

## Example

```python
from lusid.models.order_graph_block_transaction_synopsis import OrderGraphBlockTransactionSynopsis

# TODO update the JSON string below
json = "{}"
# create an instance of OrderGraphBlockTransactionSynopsis from a JSON string
order_graph_block_transaction_synopsis_instance = OrderGraphBlockTransactionSynopsis.from_json(json)
# print the JSON string representation of the object
print OrderGraphBlockTransactionSynopsis.to_json()

# convert the object into a dict
order_graph_block_transaction_synopsis_dict = order_graph_block_transaction_synopsis_instance.to_dict()
# create an instance of OrderGraphBlockTransactionSynopsis from a dict
order_graph_block_transaction_synopsis_form_dict = order_graph_block_transaction_synopsis.from_dict(order_graph_block_transaction_synopsis_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


