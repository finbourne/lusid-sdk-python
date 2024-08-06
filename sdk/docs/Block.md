# Block

A block of orders for the same instrument, intended to record for example a trader's aggregation  of outstanding orders at a given time.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ResourceId**](ResourceId.md) |  | 
**order_ids** | [**List[ResourceId]**](ResourceId.md) | The related order ids. | 
**properties** | [**Dict[str, PerpetualProperty]**](PerpetualProperty.md) | Client-defined properties associated with this block. | [optional] 
**instrument_identifiers** | **Dict[str, str]** | The instrument ordered. | 
**lusid_instrument_id** | **str** | The LUSID instrument id for the instrument ordered. | 
**quantity** | **float** | The total quantity of given instrument ordered. | 
**side** | **str** | The client&#39;s representation of the block&#39;s side (buy, sell, short, etc) | 
**type** | **str** | The block order&#39;s type (examples: Limit, Market, ...) | 
**time_in_force** | **str** | The block orders&#39; time in force (examples: Day, GoodTilCancel, ...) | 
**created_date** | **datetime** | The date on which the block was made | 
**limit_price** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | [optional] 
**stop_price** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | [optional] 
**version** | [**Version**](Version.md) |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.block import Block

# TODO update the JSON string below
json = "{}"
# create an instance of Block from a JSON string
block_instance = Block.from_json(json)
# print the JSON string representation of the object
print Block.to_json()

# convert the object into a dict
block_dict = block_instance.to_dict()
# create an instance of Block from a dict
block_form_dict = block.from_dict(block_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


