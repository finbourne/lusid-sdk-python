# RelatedEntity

Information about the other related entity in the relationship

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_type** | **str** | The type of the entity. | 
**entity_id** | **dict(str, str)** | The identifier of the other related entity in the relationship. It contains &#39;scope&#39; and &#39;code&#39; as keys for identifiers of a Portfolio or Portfolio Group, or &#39;idTypeScope&#39;, &#39;idTypeCode&#39;, &#39;code&#39; as keys for identifiers of a Person or Legal Entity. | 
**display_name** | **str** | The display name of the entity. | 
**properties** | [**dict(str, ModelProperty)**](ModelProperty.md) | The properties of the entity. This field is empty until further notice. | [optional] 
**scope** | **str** | The scope of the identifier | [optional] 
**lusid_unique_id** | [**LusidUniqueId**](LusidUniqueId.md) |  | [optional] 
**identifiers** | [**list[EntityIdentifier]**](EntityIdentifier.md) | The identifiers of the related entity in the relationship. | 
**href** | **str** | The link to the entity. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


