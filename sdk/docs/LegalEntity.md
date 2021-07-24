# LegalEntity

Representation of Legal Entity on LUSID API

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | The display name of the Legal Entity | [optional] 
**description** | **str** | The description of the Legal Entity | [optional] 
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**lusid_legal_entity_id** | **str** | The unique LUSID Legal Entity Identifier (LULEID) of the Legal Entity. This field is not populated until further notice. | [optional] 
**identifiers** | [**dict(str, ModelProperty)**](ModelProperty.md) | Unique client-defined identifiers of the Legal Entity. | [optional] 
**properties** | [**dict(str, ModelProperty)**](ModelProperty.md) | A set of properties associated to the Legal Entity. | [optional] 
**version** | [**Version**](Version.md) |  | [optional] 
**links** | [**list[Link]**](Link.md) | Collection of links. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


