# StagedModificationsRequestedChangeInterval


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute_name** | **str** | Name of the property the change applies to. | [optional] 
**effective_range** | [**StagedModificationEffectiveRange**](StagedModificationEffectiveRange.md) |  | [optional] 
**previous_value** | [**PropertyValue**](PropertyValue.md) |  | [optional] 
**new_value** | [**PropertyValue**](PropertyValue.md) |  | [optional] 
**as_at_basis** | **str** | Whether the change represents the modification when the request was made or the modification as it would be at the latest time. | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.staged_modifications_requested_change_interval import StagedModificationsRequestedChangeInterval

# TODO update the JSON string below
json = "{}"
# create an instance of StagedModificationsRequestedChangeInterval from a JSON string
staged_modifications_requested_change_interval_instance = StagedModificationsRequestedChangeInterval.from_json(json)
# print the JSON string representation of the object
print StagedModificationsRequestedChangeInterval.to_json()

# convert the object into a dict
staged_modifications_requested_change_interval_dict = staged_modifications_requested_change_interval_instance.to_dict()
# create an instance of StagedModificationsRequestedChangeInterval from a dict
staged_modifications_requested_change_interval_form_dict = staged_modifications_requested_change_interval.from_dict(staged_modifications_requested_change_interval_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


