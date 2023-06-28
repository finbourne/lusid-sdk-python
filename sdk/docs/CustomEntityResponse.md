# CustomEntityResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**entity_type** | **str** | The type of custom entity this is. | 
**version** | [**Version**](Version.md) |  | 
**display_name** | **str** | A display label for the custom entity. | 
**description** | **str** | A description of the custom entity. | [optional] 
**identifiers** | [**list[CustomEntityId]**](CustomEntityId.md) | The identifiers the custom entity will be upserted with. | 
**fields** | [**list[CustomEntityField]**](CustomEntityField.md) | The fields that decorate the custom entity. | 
**relationships** | [**list[Relationship]**](Relationship.md) | A set of relationships associated to the custom entity. | 
**links** | [**list[Link]**](Link.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


