# CheckStepRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** | The label of the compliance step | 
**compliance_step_type_request** | **str** | . The available values are: FilterStepRequest, GroupByStepRequest, GroupFilterStepRequest, BranchStepRequest, CheckStepRequest, PercentCheckStepRequest | 

## Example

```python
from lusid.models.check_step_request import CheckStepRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CheckStepRequest from a JSON string
check_step_request_instance = CheckStepRequest.from_json(json)
# print the JSON string representation of the object
print CheckStepRequest.to_json()

# convert the object into a dict
check_step_request_dict = check_step_request_instance.to_dict()
# create an instance of CheckStepRequest from a dict
check_step_request_form_dict = check_step_request.from_dict(check_step_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


