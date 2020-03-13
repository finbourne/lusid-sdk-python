# StructuredMarketData

An item of structured market data that is to be inserted into Lusid. This will typically be a Json or Xml document that  contains a set of market quotes (tradables) that can be used to construct a composite view of a market property such as the  interest rates over time; commonly referred to as an interest rate, projection or discount curve. Other examples include  volatility surfaces and credit spread curves.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document_format** | **str** | The format of the accompanying document. | 
**version** | **str** | The semantic version of the document format; MAJOR.MINOR.PATCH | [optional] 
**name** | **str** | The name or description for the document | [optional] 
**document** | **str** | The document that will be stored (or retrieved) and which describes a structured market data entity such as a credit or interest rate curve | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


