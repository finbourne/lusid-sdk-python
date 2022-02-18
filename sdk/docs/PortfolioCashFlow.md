# PortfolioCashFlow

The details for the cashflow for a given portfolio.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_by_id** | **int** | The groupBy subHoldings and currency. | 
**sequence_number** | **int** | Sequence number determining the order of the cash flow records. | 
**effective_date** | **datetime** | Indicates the date when the cash-flow settles. | [optional] 
**sub_holding_keys** | [**dict(str, PerpetualProperty)**](PerpetualProperty.md) | The sub-holding properties which identify the holding. Each property will be from the &#39;Transaction&#39; domain. These are configured on a transaction portfolio. | [optional] 
**type** | **str** | Indicates the record type (Closed, Open, Activity). | 
**movement_name** | **str** | Indicates the specific movement of the transaction that generated this cash flow. | 
**cashflow** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | 
**balance** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | 
**fx_rate** | **float** | Exchange rate between the currency of this cash flow and the reporting currency. | 
**cashflow_reporting_currency** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | 
**balance_reporting_currency** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | 
**translation_gain_loss** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | 
**cost_basis_reporting_currency** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | 
**transaction** | [**Transaction**](Transaction.md) |  | [optional] 
**unrealised_gain_loss_reporting_currency** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | 
**links** | [**list[Link]**](Link.md) | Collection of links. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


