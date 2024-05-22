# GroupFilterStepRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** | The label of the compliance step | 
**compliance_step_type_request** | **str** | . The available values are: FilterStepRequest, GroupByStepRequest, GroupFilterStepRequest, BranchStepRequest, CheckStepRequest | 

## Example

```python
from lusid.models.group_filter_step_request import GroupFilterStepRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GroupFilterStepRequest from a JSON string
group_filter_step_request_instance = GroupFilterStepRequest.from_json(json)
# print the JSON string representation of the object
print GroupFilterStepRequest.to_json()

# convert the object into a dict
group_filter_step_request_dict = group_filter_step_request_instance.to_dict()
# create an instance of GroupFilterStepRequest from a dict
group_filter_step_request_form_dict = group_filter_step_request.from_dict(group_filter_step_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


