# RelationshipDefinition


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | [**Version**](Version.md) |  | [optional] 
**relationship_definition_id** | [**ResourceId**](ResourceId.md) |  | 
**source_entity_type** | **str** | The entity type of the source entity object. | 
**target_entity_type** | **str** | The entity type of the target entity object. | 
**display_name** | **str** | The display name of the relationship. | 
**outward_description** | **str** | The description to relate source entity object and target entity object | 
**inward_description** | **str** | The description to relate target entity object and source entity object | 
**life_time** | **str** | Describes how the relationships can change over time. | 
**relationship_cardinality** | **str** | Describes the cardinality of the relationship between source entity and target entity. | 
**links** | [**list[Link]**](Link.md) | Collection of links. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


