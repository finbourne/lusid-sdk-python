# PropertyDefinition

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**key** | **str** | The property key which uniquely identifies the property. The format for the property key is {domain}/{scope}/{code}, e.g. &#39;Portfolio/Manager/Id&#39;. | [optional] 
**value_type** | **str** | The type of values that can be associated with this property. This is defined by the property&#39;s data type. | [optional] 
**value_required** | **bool** | Whether or not a value is always required for this property. | [optional] 
**display_name** | **str** | The display name of the property. | [optional] 
**data_type_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**life_time** | **str** | Describes how the property&#39;s values can change over time. | [optional] 
**type** | **str** | The type of the property. | [optional] 
**unit_schema** | **str** | The units that can be associated with the property&#39;s values. This is defined by the property&#39;s data type. | [optional] 
**domain** | **str** | The domain that the property exists in. | [optional] 
**scope** | **str** | The scope that the property exists in. | [optional] 
**code** | **str** | The code of the property. Together with the domain and scope this uniquely identifies the property. | [optional] 
**constraint_style** | **str** | Describes the uniqueness and cardinality of the property for entity objects under the property domain specified in Key. | [optional] 
**links** | [**list[Link]**](Link.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


