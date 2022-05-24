# TransactionConfigurationMovementDataRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**movement_types** | **str** | . The available values are: Settlement, Traded, StockMovement, FutureCash, Commitment, Receivable, CashSettlement, CashForward, CashCommitment, CashReceivable, Accrual, CashAccrual, ForwardFx, CashFxForward, UnsettledCashTypes, Carry, CarryAsPnl, VariationMargin | 
**side** | **str** | The movement side | 
**direction** | **int** | The movement direction | 
**properties** | [**dict(str, PerpetualProperty)**](PerpetualProperty.md) | The properties associated with the underlying Movement. | [optional] 
**mappings** | [**list[TransactionPropertyMappingRequest]**](TransactionPropertyMappingRequest.md) | This allows you to map a transaction property to a property on the underlying holding. | [optional] 
**name** | **str** | The movement name (optional) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


