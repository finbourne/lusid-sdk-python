# AllocationRequest

A request to create or update an Allocation.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**properties** | [**Dict[str, PerpetualProperty]**](PerpetualProperty.md) | Client-defined properties associated with this allocation. | [optional] 
**instrument_identifiers** | **Dict[str, str]** | The instrument allocated. | 
**quantity** | **float** | The quantity of given instrument allocated. | 
**portfolio_id** | [**ResourceId**](ResourceId.md) |  | 
**allocated_order_id** | [**ResourceId**](ResourceId.md) |  | 
**id** | [**ResourceId**](ResourceId.md) |  | 
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

## Example

```python
from lusid.models.allocation_request import AllocationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AllocationRequest from a JSON string
allocation_request_instance = AllocationRequest.from_json(json)
# print the JSON string representation of the object
print AllocationRequest.to_json()

# convert the object into a dict
allocation_request_dict = allocation_request_instance.to_dict()
# create an instance of AllocationRequest from a dict
allocation_request_form_dict = allocation_request.from_dict(allocation_request_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


