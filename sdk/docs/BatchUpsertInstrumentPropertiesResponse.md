# BatchUpsertInstrumentPropertiesResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | **dict(str, list[ModelProperty])** | The properties that have been successfully upserted | 
**failed** | [**dict(str, ErrorDetail)**](ErrorDetail.md) | The properties that could not be upserted along with a reason for their failure. | 
**as_at_date** | **datetime** | The as-at datetime at which properties were created or updated. | 
**links** | [**list[Link]**](Link.md) | Collection of links. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


