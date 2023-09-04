# TranslateEntitiesInlinedRequest

Request to translate financial entities with a given script body.  The output of the translation is validated against a schema specified in the request.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_payloads** | [**dict(str, TranslationInput)**](TranslationInput.md) | Entity payloads to be translated indexed by (ephemeral) unique correlation ids. | 
**script_body** | **str** | The body of the translation script to use for translating the entities. | 
**schema** | [**DialectSchema**](DialectSchema.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


