# BlockAndOrderRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**block_id** | [**ResourceId**](ResourceId.md) |  | 
**order_id** | [**ResourceId**](ResourceId.md) |  | 
**order_properties** | [**Dict[str, PerpetualProperty]**](PerpetualProperty.md) | Client-defined properties associated with this order. | [optional] 
**block_properties** | [**Dict[str, PerpetualProperty]**](PerpetualProperty.md) | Client-defined properties associated with this block. | [optional] 
**instrument_identifiers** | **Dict[str, str]** | The instrument ordered. | 
**quantity** | **float** | The quantity of given instrument ordered. | 
**side** | **str** | The client&#39;s representation of the order&#39;s side (buy, sell, short, etc) | 
**order_book_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**portfolio_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**state** | **str** | The order&#39;s state (examples: New, PartiallyFilled, ...) | [optional] 
**type** | **str** | The order&#39;s type (examples: Limit, Market, ...) | [optional] 
**time_in_force** | **str** | The order&#39;s time in force (examples: Day, GoodTilCancel, ...) | [optional] 
**var_date** | **datetime** | The date on which the order was made | [optional] 
**price** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | [optional] 
**limit_price** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | [optional] 
**stop_price** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | [optional] 
**order_instruction** | [**ResourceId**](ResourceId.md) |  | [optional] 
**package** | [**ResourceId**](ResourceId.md) |  | [optional] 

## Example

```python
from lusid.models.block_and_order_request import BlockAndOrderRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BlockAndOrderRequest from a JSON string
block_and_order_request_instance = BlockAndOrderRequest.from_json(json)
# print the JSON string representation of the object
print BlockAndOrderRequest.to_json()

# convert the object into a dict
block_and_order_request_dict = block_and_order_request_instance.to_dict()
# create an instance of BlockAndOrderRequest from a dict
block_and_order_request_form_dict = block_and_order_request.from_dict(block_and_order_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


