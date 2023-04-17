# GetComplexMarketDataResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**values** | [**dict(str, ComplexMarketData)**](ComplexMarketData.md) | The set of values that were successfully retrieved. | [optional] 
**failed** | [**dict(str, ErrorDetail)**](ErrorDetail.md) | The set of values that could not be retrieved due along with a reason for this, e.g badly formed request. | [optional] 
**links** | [**list[Link]**](Link.md) | Collection of links. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


