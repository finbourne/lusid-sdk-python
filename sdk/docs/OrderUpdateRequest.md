# OrderUpdateRequest

A request to create or update a Order.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ResourceId**](ResourceId.md) |  | 
**quantity** | **float** | The quantity of given instrument ordered. | [optional] 
**portfolio_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**properties** | [**Dict[str, PerpetualProperty]**](PerpetualProperty.md) | Client-defined properties associated with this order. | [optional] 
**price** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | [optional] 
**limit_price** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | [optional] 
**stop_price** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | [optional] 

## Example

```python
from lusid.models.order_update_request import OrderUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OrderUpdateRequest from a JSON string
order_update_request_instance = OrderUpdateRequest.from_json(json)
# print the JSON string representation of the object
print OrderUpdateRequest.to_json()

# convert the object into a dict
order_update_request_dict = order_update_request_instance.to_dict()
# create an instance of OrderUpdateRequest from a dict
order_update_request_form_dict = order_update_request.from_dict(order_update_request_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


