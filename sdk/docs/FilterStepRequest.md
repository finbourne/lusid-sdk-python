# FilterStepRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** | The label of the compliance step | 
**compliance_step_type_request** | **str** | . The available values are: FilterStepRequest, GroupByStepRequest, GroupFilterStepRequest, BranchStepRequest, CheckStepRequest, PercentCheckStepRequest | 

## Example

```python
from lusid.models.filter_step_request import FilterStepRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FilterStepRequest from a JSON string
filter_step_request_instance = FilterStepRequest.from_json(json)
# print the JSON string representation of the object
print FilterStepRequest.to_json()

# convert the object into a dict
filter_step_request_dict = filter_step_request_instance.to_dict()
# create an instance of FilterStepRequest from a dict
filter_step_request_form_dict = filter_step_request.from_dict(filter_step_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


