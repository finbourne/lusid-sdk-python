# ExpandedGroup


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**id** | [**ResourceId**](ResourceId.md) |  | 
**display_name** | **str** | The name of the portfolio group. | 
**description** | **str** | The long form description of the portfolio group. | [optional] 
**values** | [**list[CompletePortfolio]**](CompletePortfolio.md) | The collection of resource identifiers for the portfolios contained in the portfolio group. | [optional] 
**sub_groups** | [**list[ExpandedGroup]**](ExpandedGroup.md) | The collection of resource identifiers for the portfolio groups contained in the portfolio group as sub groups. | [optional] 
**version** | [**Version**](Version.md) |  | [optional] 
**links** | [**list[Link]**](Link.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


