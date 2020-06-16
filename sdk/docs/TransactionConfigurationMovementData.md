# TransactionConfigurationMovementData

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**movement_types** | **str** | . The available values are: Settlement, Traded, StockMovement, FutureCash, Commitment, Receivable, CashSettlement, CashForward, CashCommitment, CashReceivable, Accrual, CashAccrual, ForwardFx, CashFxForward, UnsettledCashTypes | 
**side** | **str** | The Movement Side | 
**direction** | **int** | The Movement direction | 
**properties** | [**dict(str, PerpetualProperty)**](PerpetualProperty.md) |  | [optional] 
**mappings** | [**list[TransactionPropertyMapping]**](TransactionPropertyMapping.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


