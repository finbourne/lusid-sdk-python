# CompositeBreakdownRequest

The request used in the GetCompositeBreakdown.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**return_ids** | [**list[ResourceId]**](ResourceId.md) | The Scope and code of the returns. | [optional] 
**recipe_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**composite_method** | **str** | The method used to calculate the Portfolio performance: Equal/Asset. | [optional] 
**period** | **str** | The type of the returns used to calculate the aggregation result: Daily/Monthly. | [optional] 
**holiday_calendars** | **list[str]** | The holiday calendar(s) that should be used in determining the date schedule. Holiday calendar(s) are supplied by their codes, for example, &#39;CoppClark&#39;. Note that when the calendars are not available (e.g. when the user has insufficient permissions), a recipe setting will be used to determine whether the whole batch should then fail or whether the calendar not being available should simply be ignored. | [optional] 
**currency** | **str** | Optional - either a string or a property. If provided, the results will be converted to the specified currency | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


