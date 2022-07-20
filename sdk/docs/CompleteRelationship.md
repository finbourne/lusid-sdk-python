# CompleteRelationship

Representation of a relationship containing details of source and target entities, and both outward and inward descriptions.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**version** | [**Version**](Version.md) |  | [optional] 
**relationship_definition_id** | [**ResourceId**](ResourceId.md) |  | 
**source_entity** | [**RelatedEntity**](RelatedEntity.md) |  | 
**target_entity** | [**RelatedEntity**](RelatedEntity.md) |  | 
**outward_description** | **str** | Description of the relationship based on relationship definition&#39;s outward description. | 
**inward_description** | **str** | Description of the relationship based on relationship definition&#39;s inward description. | 
**effective_from** | **datetime** | The effective datetime from which the relationship is valid. | [optional] 
**effective_until** | **datetime** | The effective datetime to which the relationship is valid until. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


