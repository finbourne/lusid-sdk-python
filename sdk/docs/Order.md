# Order

An Order for a certain quantity of a specific instrument

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**properties** | [**Dict[str, PerpetualProperty]**](PerpetualProperty.md) | Client-defined properties associated with this order. | [optional] 
**version** | [**Version**](Version.md) |  | [optional] 
**instrument_identifiers** | **Dict[str, str]** | The instrument ordered. | 
**quantity** | **float** | The quantity of given instrument ordered. | 
**side** | **str** | The client&#39;s representation of the order&#39;s side (buy, sell, short, etc) | 
**order_book_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**portfolio_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**id** | [**ResourceId**](ResourceId.md) |  | 
**instrument_scope** | **str** | The scope in which the instrument lies | [optional] 
**lusid_instrument_id** | **str** | The LUSID instrument id for the instrument ordered. | 
**state** | **str** | The order&#39;s state (examples: New, PartiallyFilled, ...) | [optional] 
**type** | **str** | The order&#39;s type (examples: Limit, Market, ...) | [optional] 
**time_in_force** | **str** | The order&#39;s time in force (examples: Day, GoodTilCancel, ...) | [optional] 
**var_date** | **datetime** | The date on which the order was made | [optional] 
**price** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | [optional] 
**limit_price** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | [optional] 
**stop_price** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | [optional] 
**order_instruction_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**package_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.order import Order

# TODO update the JSON string below
json = "{}"
# create an instance of Order from a JSON string
order_instance = Order.from_json(json)
# print the JSON string representation of the object
print Order.to_json()

# convert the object into a dict
order_dict = order_instance.to_dict()
# create an instance of Order from a dict
order_form_dict = order.from_dict(order_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


