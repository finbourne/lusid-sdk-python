# ChangeHistory

A group of changes made by the same person at the same time.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** | The unique identifier of the user that made the change. | 
**modified_as_at** | **datetime** | The date/time of the change. | 
**request_id** | **str** | The unique identifier of the request that the changes were part of. | 
**action** | **str** | The action performed on the transaction, either created, updated, or deleted. The available values are: Create, Update, Delete | 
**changes** | [**list[ChangeItem]**](ChangeItem.md) | The collection of changes that were made. | 
**links** | [**list[Link]**](Link.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


