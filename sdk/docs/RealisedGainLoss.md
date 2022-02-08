# RealisedGainLoss


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instrument_scope** | **str** | The scope in which the instrument lies. | 
**instrument_uid** | **str** | The unqiue Lusid Instrument Id (LUID) of the instrument that this gain or loss is associated with. | 
**units** | **float** | The number of units of the associated instrument against which the gain or loss has been realised. | 
**purchase_trade_date** | **datetime** | The effective datetime that the units associated with this gain or loss where originally purchased. | [optional] [readonly] 
**purchase_settlement_date** | **datetime** | The effective datetime that the units associated with this gain or loss where originally settled. | [optional] [readonly] 
**purchase_price** | **float** | The purchase price of each unit associated with this gain or loss. | [optional] 
**cost_trade_ccy** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | 
**cost_portfolio_ccy** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | 
**realised_trade_ccy** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | 
**realised_total** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | 
**realised_market** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | [optional] 
**realised_currency** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


