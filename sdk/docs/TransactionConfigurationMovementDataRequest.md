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
**movement_options** | **list[str]** | Allows extra specifications for the movement. The only option currently available is &#39;DirectAdjustment&#39;. A movement type of &#39;StockMovement&#39; with an option of &#39;DirectAdjusment&#39; will allow you to adjust the unitsof a holding without affecting its cost base. You will, therefore, be able to reflect the impact of a stock split by loading a Transaction. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


