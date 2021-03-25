# CreateRelationDefinitionRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scope** | **str** | The scope that the relation exists in. | 
**code** | **str** | The code of the relation. Together with the scope this uniquely defines the relation. | 
**source_entity_domain** | **str** | The entity domain of the source entity object must be, allowed values are \&quot;Portfolio\&quot; and \&quot;Person\&quot; | 
**target_entity_domain** | **str** | The entity domain of the target entity object must be, allowed values are \&quot;Portfolio\&quot; and \&quot;Person\&quot; | 
**display_name** | **str** | The display name of the relation. | 
**outward_description** | **str** | The description to relate source entity object and target entity object. | 
**inward_description** | **str** | The description to relate target entity object and source entity object. | 
**life_time** | **str** | Describes how the relations can change over time, allowed values are \&quot;Perpetual\&quot; and \&quot;TimeVariant\&quot; | [optional] 
**constraint_style** | **str** | Describes the uniqueness and cardinality for relations with a specific source entity object and relations under this definition. Allowed values are \&quot;Property\&quot; and \&quot;Collection\&quot;, defaults to \&quot;Collection\&quot; if not specified. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


