# Allocation

An Allocation of a certain quantity of a specific instrument against an originating  Order.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ResourceId**](ResourceId.md) |  | 
**allocated_order_id** | [**ResourceId**](ResourceId.md) |  | 
**portfolio_id** | [**ResourceId**](ResourceId.md) |  | 
**quantity** | **float** | The quantity of given instrument allocated. | 
**instrument_identifiers** | **Dict[str, str]** | The instrument allocated. | 
**version** | [**Version**](Version.md) |  | [optional] 
**properties** | [**Dict[str, PerpetualProperty]**](PerpetualProperty.md) | Client-defined properties associated with this allocation. | [optional] 
**instrument_scope** | **str** | The scope in which the instrument lies | [optional] 
**lusid_instrument_id** | **str** | The LUSID instrument id for the instrument allocated. | 
**placement_ids** | [**List[ResourceId]**](ResourceId.md) | A placement - also known as an order placed in the market - associated with this allocation. | [optional] 
**state** | **str** | The state of this allocation. | [optional] 
**side** | **str** | The side of this allocation (examples: Buy, Sell, ...). | [optional] 
**type** | **str** | The type of order associated with this allocation (examples: Limit, Market, ...). | [optional] 
**settlement_date** | **datetime** | The settlement date for this allocation. | [optional] 
**var_date** | **datetime** | The date of this allocation. | [optional] 
**price** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | [optional] 
**settlement_currency** | **str** | The settlement currency of this allocation. | [optional] 
**settlement_currency_fx_rate** | **float** | The settlement currency to allocation currency FX rate. | [optional] 
**counterparty** | **str** | The counterparty for this allocation. | [optional] 
**execution_ids** | [**List[ResourceId]**](ResourceId.md) | The executions associated with this allocation | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.allocation import Allocation

# TODO update the JSON string below
json = "{}"
# create an instance of Allocation from a JSON string
allocation_instance = Allocation.from_json(json)
# print the JSON string representation of the object
print Allocation.to_json()

# convert the object into a dict
allocation_dict = allocation_instance.to_dict()
# create an instance of Allocation from a dict
allocation_form_dict = allocation.from_dict(allocation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


