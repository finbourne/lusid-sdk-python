# AnnulQuotesResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**values** | **dict(str, datetime)** | The quotes which have been successfully deleted along with the asAt datetime at which the deletion was committed to LUSID. | [optional] 
**failed** | [**dict(str, ErrorDetail)**](ErrorDetail.md) | The quotes that could not be deleted along with a reason for their failure. | [optional] 
**links** | [**list[Link]**](Link.md) | Collection of links. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


