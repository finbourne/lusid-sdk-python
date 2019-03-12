# PortfolioHolding

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instrument_uid** | **str** | Unique instrument identifier | 
**sub_holding_keys** | [**list[PerpetualProperty]**](PerpetualProperty.md) |  | [optional] 
**properties** | [**list[ModelProperty]**](ModelProperty.md) |  | [optional] 
**holding_type** | **str** | Type of holding, eg Position, Balance, CashCommitment, Receivable, ForwardFX | 
**units** | **float** | Quantity of holding | 
**settled_units** | **float** | Settled quantity of holding | 
**cost** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | 
**cost_portfolio_ccy** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | 
**transaction** | [**Transaction**](Transaction.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


