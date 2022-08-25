# ChangeItem

Information about a change to a field / property.  At least one of 'PreviousValue' or 'NewValue' will be set.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field_name** | **str** | The name of the field or property that has been changed. | 
**previous_value** | **str** | The previous value for this field / property. | [optional] 
**new_value** | **str** | The new value for this field / property. | [optional] 
**effective_from** | **datetime** | The market data time, i.e. the time to run the change from. | [optional] 
**effective_until** | **datetime** | The market data time, i.e. the time to run the change until. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


