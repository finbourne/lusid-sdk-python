# A2BMovementRecord

A2B Movement Record - shows A2B category based changes relating to a specific movement

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**portfolio_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**holding_type** | **str** | The code for the type of the holding e.g. P, B, C, R, F etc. | [optional] 
**instrument_scope** | **str** | The unique Lusid Instrument Id (LUID) of the instrument that the holding is in. | [optional] 
**instrument_uid** | **str** | The unique Lusid Instrument Id (LUID) of the instrument that the holding is in. | [optional] 
**sub_holding_keys** | [**dict(str, PerpetualProperty)**](PerpetualProperty.md) | The sub-holding properties which identify the holding. Each property will be from the &#39;Transaction&#39; domain. These are configured on a transaction portfolio. | [optional] 
**currency** | **str** | The holding currency. | [optional] 
**transaction_id** | **str** | The unique identifier for the transaction. | [optional] 
**movement_name** | **str** | The name of the movement. | [optional] 
**effective_date** | **datetime** | The date of the movement. | [optional] 
**units** | **float** | The number of units of the instrument that are affected by the movement. | [optional] 
**start** | [**A2BCategory**](A2BCategory.md) |  | [optional] 
**flows** | [**A2BCategory**](A2BCategory.md) |  | [optional] 
**gains** | [**A2BCategory**](A2BCategory.md) |  | [optional] 
**carry** | [**A2BCategory**](A2BCategory.md) |  | [optional] 
**end** | [**A2BCategory**](A2BCategory.md) |  | [optional] 
**properties** | [**dict(str, ModelProperty)**](ModelProperty.md) | The properties which have been requested to be decorated onto the holding. These will be from the &#39;Instrument&#39; domain. | [optional] 
**group_id** | **str** | Arbitrary string that can be used to cross reference an entry in the A2B report with activity in the A2B-Movements. This should be used purely as a token. The content should not be relied upon. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


