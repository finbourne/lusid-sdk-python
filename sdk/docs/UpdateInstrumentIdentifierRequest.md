# UpdateInstrumentIdentifierRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of the identifier to upsert. This must be one of the code types marked as   allowable for instrument identifiers. | [optional] 
**value** | **str** | The value of the identifier. If set to &#x60;null&#x60;, this will remove the identifier completely.  Note that, if an instrument only has one identifier, it is an error to remove this. | [optional] 
**effective_at** | **str** | The date at which the identifier modification is to be effective from. If unset, will  default to &#x60;now&#x60;. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


