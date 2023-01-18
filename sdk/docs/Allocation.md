# Allocation

An Allocation of a certain quantity of a specific instrument against an originating  Order.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ResourceId**](ResourceId.md) |  | 
**allocated_order_id** | [**ResourceId**](ResourceId.md) |  | 
**portfolio_id** | [**ResourceId**](ResourceId.md) |  | 
**quantity** | **float** | The quantity of given instrument allocated. | 
**instrument_identifiers** | **dict(str, str)** | The instrument allocated. | 
**version** | [**Version**](Version.md) |  | [optional] 
**properties** | [**dict(str, PerpetualProperty)**](PerpetualProperty.md) | Client-defined properties associated with this allocation. | [optional] 
**instrument_scope** | **str** | The scope in which the instrument lies | [optional] 
**lusid_instrument_id** | **str** | The LUSID instrument id for the instrument allocated. | 
**placement_ids** | [**list[ResourceId]**](ResourceId.md) | A placement - also known as an order placed in the market - associated with this allocation. | [optional] 
**state** | **str** | The state of this allocation. | [optional] 
**side** | **str** | The side of this allocation (examples: Buy, Sell, ...). | [optional] 
**type** | **str** | The type of order associated with this allocation (examples: Limit, Market, ...). | [optional] 
**settlement_date** | **datetime** | The settlement date for this allocation. | [optional] 
**date** | **datetime** | The date of this allocation. | [optional] 
**price** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | [optional] 
**settlement_currency** | **str** | The settlement currency of this allocation. | [optional] 
**settlement_currency_fx_rate** | **float** | The settlement currency to allocation currency FX rate. | [optional] 
**counterparty** | **str** | The counterparty for this allocation. | [optional] 
**links** | [**list[Link]**](Link.md) | Collection of links. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


