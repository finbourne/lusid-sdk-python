# ChangeIntervalWithOrderManagementDetail

Defines a change that occured for an entity, with extra detail about the change

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**detail** | **Dict[str, str]** | Information about the particular instance of the ChangeInterval (supplied information depends on the type of Action). Contains extra detail for order management actions such as related entity ids and compliance run details. | [optional] 
**action_description** | **str** | Description of the action performed on the entity. | [optional] 
**as_at_modified** | **datetime** | The date/time of the change. | [optional] 
**user_id_modified** | **str** | The unique identifier of the user that made the change. | [optional] 
**request_id_modified** | **str** | The unique identifier of the request that the changes were part of. | [optional] 
**reason_modified** | **str** | The reason for an entity modification. | [optional] 
**as_at_version_number** | **int** | The version number for the entity (the entity was created at version 1). This may refer to the version number of a changed related entity, not a change for the entity itself. | [optional] 
**staged_modification_id_modified** | **str** | The id of the staged modification that was approved. Will be null if the change didn&#39;t come from a staged modification. | [optional] 
**action** | **str** | The action performed on the field. | [optional] 
**attribute_name** | **str** | The name of the field or property that has been changed. | [optional] 
**previous_value** | [**PropertyValue**](PropertyValue.md) |  | [optional] 
**new_value** | [**PropertyValue**](PropertyValue.md) |  | [optional] 
**effective_range** | [**EffectiveRange**](EffectiveRange.md) |  | [optional] 

## Example

```python
from lusid.models.change_interval_with_order_management_detail import ChangeIntervalWithOrderManagementDetail

# TODO update the JSON string below
json = "{}"
# create an instance of ChangeIntervalWithOrderManagementDetail from a JSON string
change_interval_with_order_management_detail_instance = ChangeIntervalWithOrderManagementDetail.from_json(json)
# print the JSON string representation of the object
print ChangeIntervalWithOrderManagementDetail.to_json()

# convert the object into a dict
change_interval_with_order_management_detail_dict = change_interval_with_order_management_detail_instance.to_dict()
# create an instance of ChangeIntervalWithOrderManagementDetail from a dict
change_interval_with_order_management_detail_form_dict = change_interval_with_order_management_detail.from_dict(change_interval_with_order_management_detail_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


