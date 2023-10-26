# BlockRequest

A request to create or update an Order.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ResourceId**](ResourceId.md) |  | 
**order_ids** | [**List[ResourceId]**](ResourceId.md) | The related order ids. | 
**properties** | [**Dict[str, PerpetualProperty]**](PerpetualProperty.md) | Client-defined properties associated with this block. | [optional] 
**instrument_identifiers** | **Dict[str, str]** | The instrument ordered. | 
**quantity** | **float** | The total quantity of given instrument ordered. | 
**side** | **str** | The client&#39;s representation of the block&#39;s side (buy, sell, short, etc) | 
**type** | **str** | The block order&#39;s type (examples: Limit, Market, ...) | 
**time_in_force** | **str** | The block orders&#39; time in force (examples: Day, GoodTilCancel, ...) | 
**created_date** | **datetime** | The date on which the block was made | 
**limit_price** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | [optional] 
**stop_price** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | [optional] 

## Example

```python
from lusid.models.block_request import BlockRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BlockRequest from a JSON string
block_request_instance = BlockRequest.from_json(json)
# print the JSON string representation of the object
print BlockRequest.to_json()

# convert the object into a dict
block_request_dict = block_request_instance.to_dict()
# create an instance of BlockRequest from a dict
block_request_form_dict = block_request.from_dict(block_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


