# Placement

A street order for a quantity of a single instrument placed with a single market entity.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ResourceId**](ResourceId.md) |  | 
**parent_placement_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**block_ids** | [**list[ResourceId]**](ResourceId.md) | The IDs of the Blocks associated with this placement. | 
**properties** | [**dict(str, PerpetualProperty)**](PerpetualProperty.md) | Client-defined properties associated with this placement. | [optional] 
**instrument_identifiers** | **dict(str, str)** | The instrument ordered. | 
**lusid_instrument_id** | **str** | The LUSID instrument id for the instrument placement. | 
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
**version** | [**Version**](Version.md) |  | [optional] 
**links** | [**list[Link]**](Link.md) | Collection of links. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


