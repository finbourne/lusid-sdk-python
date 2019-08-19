# CreatePortfolioGroupRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | The code that the portfolio group will be created with. Together with the scope this uniquely identifies the portfolio group. | 
**values** | [**list[ResourceId]**](ResourceId.md) | The resource identifiers of the portfolios to be contained within the portfolio group. | [optional] 
**sub_groups** | [**list[ResourceId]**](ResourceId.md) | The resource identifiers of the portfolio groups to be contained within the portfolio group as sub groups. | [optional] 
**display_name** | **str** | The name of the portfolio group. | 
**description** | **str** | A long form description of the portfolio group. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


