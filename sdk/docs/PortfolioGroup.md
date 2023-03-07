# PortfolioGroup


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**id** | [**ResourceId**](ResourceId.md) |  | 
**display_name** | **str** | The name of the portfolio group. | 
**description** | **str** | The long form description of the portfolio group. | [optional] 
**created** | **datetime** | The effective datetime at which the portfolio group was created. No portfolios or sub groups can be added to the group before this date. | [optional] 
**portfolios** | [**list[ResourceId]**](ResourceId.md) | The collection of resource identifiers for the portfolios contained in the portfolio group. | [optional] 
**sub_groups** | [**list[ResourceId]**](ResourceId.md) | The collection of resource identifiers for the portfolio groups contained in the portfolio group as sub groups. | [optional] 
**relationships** | [**list[Relationship]**](Relationship.md) | A set of relationships associated to the portfolio group. | [optional] 
**version** | [**Version**](Version.md) |  | [optional] 
**links** | [**list[Link]**](Link.md) | Collection of links. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


