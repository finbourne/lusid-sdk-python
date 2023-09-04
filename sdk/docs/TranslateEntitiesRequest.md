# TranslateEntitiesRequest

Request to translate financial entities with a specified script stored in LUSID,  specified in the request by its id. The output of the translation is validated against a dialect stored in LUSID,  again specified in the request by its id.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_payloads** | [**dict(str, TranslationInput)**](TranslationInput.md) | Entity payloads to be translated, indexed by (ephemeral) unique correlation ids. | 
**script_id** | [**TranslationScriptId**](TranslationScriptId.md) |  | 
**dialect_id** | [**DialectId**](DialectId.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


