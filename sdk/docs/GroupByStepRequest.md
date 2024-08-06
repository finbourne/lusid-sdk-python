# GroupByStepRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** | The label of the compliance step | 
**compliance_step_type_request** | **str** | . The available values are: FilterStepRequest, GroupByStepRequest, GroupFilterStepRequest, BranchStepRequest, CheckStepRequest, PercentCheckStepRequest | 

## Example

```python
from lusid.models.group_by_step_request import GroupByStepRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GroupByStepRequest from a JSON string
group_by_step_request_instance = GroupByStepRequest.from_json(json)
# print the JSON string representation of the object
print GroupByStepRequest.to_json()

# convert the object into a dict
group_by_step_request_dict = group_by_step_request_instance.to_dict()
# create an instance of GroupByStepRequest from a dict
group_by_step_request_form_dict = group_by_step_request.from_dict(group_by_step_request_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


