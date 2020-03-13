# PortfolioHolding

A list of holdings.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instrument_uid** | **str** | The unqiue Lusid Instrument Id (LUID) of the instrument that the holding is in. | 
**sub_holding_keys** | [**dict(str, PerpetualProperty)**](PerpetualProperty.md) | The sub-holding properties which identify the holding. Each property will be from the &#39;Transaction&#39; domain. These are configured when a transaction portfolio is created. | [optional] 
**properties** | [**dict(str, ModelProperty)**](ModelProperty.md) | The properties which have been requested to be decorated onto the holding. These will be from the &#39;Instrument&#39; or &#39;Holding&#39; domain. | [optional] 
**holding_type** | **str** | The type of the holding e.g. Position, Balance, CashCommitment, Receivable, ForwardFX etc. | 
**units** | **float** | The total number of units of the holding. | 
**settled_units** | **float** | The total number of settled units of the holding. | 
**cost** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | 
**cost_portfolio_ccy** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | 
**transaction** | [**Transaction**](Transaction.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


