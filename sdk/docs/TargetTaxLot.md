# TargetTaxLot

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**units** | **float** | The number of units of the instrument in this tax-lot. | 
**cost** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | [optional] 
**portfolio_cost** | **float** | The total cost of the tax-lot in the transaction portfolio&#39;s base currency. | [optional] 
**price** | **float** | The purchase price of each unit of the instrument held in this tax-lot. This forms part of the unique key required for multiple tax-lots. | [optional] 
**purchase_date** | **datetime** | The purchase date of this tax-lot. This forms part of the unique key required for multiple tax-lots. | [optional] 
**settlement_date** | **datetime** | The settlement date of the tax-lot&#39;s opening transaction. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


