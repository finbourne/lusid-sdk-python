# ModelProperty

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The key of the property. This takes the format {domain}/{scope}/{code} e.g. &#39;Instrument/system/Name&#39; or &#39;Transaction/strategy/quantsignal&#39;. | 
**value** | [**PropertyValue**](PropertyValue.md) |  | 
**effective_from** | **datetime** | The effective datetime from which the property is valid. | [optional] 
**effective_until** | **datetime** | The effective datetime until which the property is valid. If not supplied this will be valid indefinitely, potentially overwriting values with EffectiveFrom&#39;s in the future. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


