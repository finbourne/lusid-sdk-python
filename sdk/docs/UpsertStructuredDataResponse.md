# UpsertStructuredDataResponse

Response from upserting structured data document
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The specifc Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**values** | **dict(str, datetime)** | The set of values that were successfully retrieved. | [optional] 
**failed** | [**dict(str, ErrorDetail)**](ErrorDetail.md) | The set of values that could not be retrieved due along with a reason for this, e.g badly formed request. | [optional] 
**links** | [**list[Link]**](Link.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


