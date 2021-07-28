# UpsertReturnsResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | [**Version**](Version.md) |  | 
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**values** | **list[dict(str, datetime)]** | The set of values that were successfully retrieved. | [optional] 
**failed** | **list[dict(str, ErrorDetail)]** | The set of values that could not be retrieved due along with a reason for this, e.g badly formed request. | [optional] 
**links** | [**list[Link]**](Link.md) | Collection of links. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


