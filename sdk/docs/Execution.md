# Execution

The record of a number of executions against a single Placement (directly analogous to  a partial or full fill against a street order).

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ResourceId**](ResourceId.md) |  | 
**placement_id** | [**ResourceId**](ResourceId.md) |  | 
**properties** | [**dict(str, PerpetualProperty)**](PerpetualProperty.md) | Client-defined properties associated with this execution. | [optional] 
**instrument_identifiers** | **dict(str, str)** | The instrument ordered. | 
**lusid_instrument_id** | **str** | The LUSID instrument id for the instrument execution. | 
**quantity** | **float** | The quantity of given instrument ordered. | 
**state** | **str** | The state of this execution (typically a FIX state; Open, Filled, etc). | 
**side** | **str** | The side (Buy, Sell, ...) of this execution. | 
**type** | **str** | The type of this execution (Market, Limit, etc). | 
**created_date** | **datetime** | The active date of this execution. | 
**settlement_date** | **datetime** | The (optional) settlement date for this execution | [optional] 
**price** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | 
**settlement_currency** | **str** | The execution&#39;s settlement currency. | 
**settlement_currency_fx_rate** | **float** | The exectuion&#39;s settlement currency rate. | 
**counterparty** | **str** | The market entity this placement is placed with. | 
**average_price** | **float** | The average price of all executions for a given placement at the time of upsert | [optional] 
**version** | [**Version**](Version.md) |  | [optional] 
**links** | [**list[Link]**](Link.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


