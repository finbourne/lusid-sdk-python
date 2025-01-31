# BlockAndOrdersRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**block_id** | [**ResourceId**](ResourceId.md) |  | 
**orders** | [**List[BlockedOrderRequest]**](BlockedOrderRequest.md) | An order which belongs to a block. Fields common to both entities (such as instrument) should be derived from the block. | 
**block_properties** | [**Dict[str, PerpetualProperty]**](PerpetualProperty.md) | Client-defined properties associated with this block. | [optional] 
**instrument_identifiers** | **Dict[str, str]** | The instrument ordered. | 
**side** | **str** | The client&#39;s representation of the block&#39;s side (buy, sell, short, etc). BlockedOrders in the request which do not specify a side will have their side populated with this value. | [optional] 
**type** | **str** | The block order&#39;s type (examples: Limit, Market, ...) | [optional] 
**time_in_force** | **str** | The block orders&#39; time in force (examples: Day, GoodTilCancel, ...) | [optional] 
**var_date** | **datetime** | The date on which the block was made | [optional] 
**limit_price** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | [optional] 
**stop_price** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | [optional] 

## Example

```python
from lusid.models.block_and_orders_request import BlockAndOrdersRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BlockAndOrdersRequest from a JSON string
block_and_orders_request_instance = BlockAndOrdersRequest.from_json(json)
# print the JSON string representation of the object
print BlockAndOrdersRequest.to_json()

# convert the object into a dict
block_and_orders_request_dict = block_and_orders_request_instance.to_dict()
# create an instance of BlockAndOrdersRequest from a dict
block_and_orders_request_form_dict = block_and_orders_request.from_dict(block_and_orders_request_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


