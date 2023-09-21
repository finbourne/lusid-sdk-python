# UpsertLegalEntitiesResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**values** | [**dict(str, LegalEntity)**](LegalEntity.md) | The legal entities which have been successfully updated or created. | [optional] 
**failed** | [**dict(str, ErrorDetail)**](ErrorDetail.md) | The legal entities that could not be updated or created or were left unchanged without error along with a reason for their failure. | [optional] 
**links** | [**list[Link]**](Link.md) | Collection of links. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


