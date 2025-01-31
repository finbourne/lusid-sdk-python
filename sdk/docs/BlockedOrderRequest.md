# BlockedOrderRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**properties** | [**Dict[str, PerpetualProperty]**](PerpetualProperty.md) | Client-defined properties associated with this order. | [optional] 
**quantity** | **float** | The quantity of given instrument ordered. | 
**order_book_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**portfolio_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**id** | [**ResourceId**](ResourceId.md) |  | 
**state** | **str** | The order&#39;s state (examples: New, PartiallyFilled, ...) | [optional] 
**var_date** | **datetime** | The date on which the order was made | [optional] 
**price** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | [optional] 
**order_instruction** | [**ResourceId**](ResourceId.md) |  | [optional] 
**package** | [**ResourceId**](ResourceId.md) |  | [optional] 
**side** | **str** | The client&#39;s representation of the order&#39;s side (buy, sell, short, etc) | [optional] 

## Example

```python
from lusid.models.blocked_order_request import BlockedOrderRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BlockedOrderRequest from a JSON string
blocked_order_request_instance = BlockedOrderRequest.from_json(json)
# print the JSON string representation of the object
print BlockedOrderRequest.to_json()

# convert the object into a dict
blocked_order_request_dict = blocked_order_request_instance.to_dict()
# create an instance of BlockedOrderRequest from a dict
blocked_order_request_form_dict = blocked_order_request.from_dict(blocked_order_request_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


