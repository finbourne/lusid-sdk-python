# CancelledPlacementResult


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**placement_state** | [**Placement**](Placement.md) |  | [optional] 
**cancelled_child_placements** | [**List[ResourceId]**](ResourceId.md) | Child placements which have also been cancelled following cancellation of the parent | 

## Example

```python
from lusid.models.cancelled_placement_result import CancelledPlacementResult

# TODO update the JSON string below
json = "{}"
# create an instance of CancelledPlacementResult from a JSON string
cancelled_placement_result_instance = CancelledPlacementResult.from_json(json)
# print the JSON string representation of the object
print CancelledPlacementResult.to_json()

# convert the object into a dict
cancelled_placement_result_dict = cancelled_placement_result_instance.to_dict()
# create an instance of CancelledPlacementResult from a dict
cancelled_placement_result_form_dict = cancelled_placement_result.from_dict(cancelled_placement_result_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


