# UpdateInstrumentIdentifierRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The allowable instrument identifier to update, insert or remove e.g. &#39;Figi&#39;. | 
**value** | **str** | The new value of the allowable instrument identifier. If unspecified the identifier will be removed from the instrument. | [optional] 
**effective_at** | **str** | The effective datetime from which the identifier should be updated, inserted or removed. Defaults to the current LUSID system datetime if not specified. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


