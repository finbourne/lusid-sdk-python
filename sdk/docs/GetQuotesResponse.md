# GetQuotesResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**values** | [**dict(str, Quote)**](Quote.md) | The quotes which have been successfully retrieved. | [optional] 
**not_found** | [**dict(str, ErrorDetail)**](ErrorDetail.md) | The quotes that could not be found along with a reason why. | [optional] 
**failed** | [**dict(str, ErrorDetail)**](ErrorDetail.md) | The quotes that could not be retrieved due to an error along with a reason for their failure. | [optional] 
**links** | [**list[Link]**](Link.md) | Collection of links. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


