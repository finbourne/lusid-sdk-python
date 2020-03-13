# StructuredResultData

An item of structured result data that is to be inserted into Lusid. This will typically be a Json or Xml document that  contains a set of result data appropriate to a specific entity such as an instrument or potentially an index.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document_format** | **str** | The format of the accompanying document. | 
**version** | **str** | The semantic version of the document format; MAJOR.MINOR.PATCH | [optional] 
**name** | **str** | The name or description for the document | [optional] 
**document** | **str** | The document that will be stored (or retrieved) and which describes a unit result data entity such as a set of prices or yields | 
**data_map** | [**DataMapping**](DataMapping.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


