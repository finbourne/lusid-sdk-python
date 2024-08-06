# PlacementRequest

A request to create or update a Placement.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ResourceId**](ResourceId.md) |  | 
**parent_placement_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**block_ids** | [**List[ResourceId]**](ResourceId.md) | The IDs of the Blocks associated with this placement. | 
**properties** | [**Dict[str, PerpetualProperty]**](PerpetualProperty.md) | Client-defined properties associated with this order. | [optional] 
**instrument_identifiers** | **Dict[str, str]** | The instrument ordered. | 
**quantity** | **float** | The quantity of given instrument ordered. | 
**state** | **str** | The state of this placement (typically a FIX state; Open, Filled, etc). | 
**side** | **str** | The side (Buy, Sell, ...) of this placement. | 
**time_in_force** | **str** | The time in force applicable to this placement (GTC, FOK, Day, etc) | 
**type** | **str** | The type of this placement (Market, Limit, etc). | 
**created_date** | **datetime** | The active date of this placement. | 
**limit_price** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | [optional] 
**stop_price** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | [optional] 
**counterparty** | **str** | Optionally specifies the market entity this placement is placed with. | [optional] 
**execution_system** | **str** | Optionally specifies the execution system in use. | [optional] 
**entry_type** | **str** | Optionally specifies the entry type of this placement. | [optional] 

## Example

```python
from lusid.models.placement_request import PlacementRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PlacementRequest from a JSON string
placement_request_instance = PlacementRequest.from_json(json)
# print the JSON string representation of the object
print PlacementRequest.to_json()

# convert the object into a dict
placement_request_dict = placement_request_instance.to_dict()
# create an instance of PlacementRequest from a dict
placement_request_form_dict = placement_request.from_dict(placement_request_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


