# AddressDefinition


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | The display name of the address key. | [optional] 
**type** | **str** | The available values are: String, Int, Decimal, DateTime, Boolean, ResultValue, Result0D, Json | [optional] 
**description** | **str** | The description for this result. | [optional] 
**life_cycle_status** | **str** | What is the status of the address path. If it is not Production then it might be removed at some point in the future.  See the removal date for the likely timing of that if any. | [optional] 
**removal_date** | **datetime** | If the life-cycle status of the address is Deprecated then this is the date at which support of the address will be suspended.  After that date it will be removed at the earliest possible point subject to any specific contractual support and development constraints. | [optional] 
**documentation_link** | **str** | Contains a link to the documentation for this AddressDefinition in KnowledgeBase. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


