# OrderGraphBlockTransactionSynopsis

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quantity** | **float** | Total number of units booked. | 
**details** | [**List[OrderGraphBlockTransactionDetail]**](OrderGraphBlockTransactionDetail.md) | Identifiers for each transaction in this block. | 
## Example

```python
from lusid.models.order_graph_block_transaction_synopsis import OrderGraphBlockTransactionSynopsis
from typing import Any, Dict, List, Union
from pydantic.v1 import BaseModel, Field, StrictFloat, StrictInt, conlist

quantity: Union[StrictFloat, StrictInt] = # Replace with your value
details: conlist(OrderGraphBlockTransactionDetail) = # Replace with your value
order_graph_block_transaction_synopsis_instance = OrderGraphBlockTransactionSynopsis(quantity=quantity, details=details)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

