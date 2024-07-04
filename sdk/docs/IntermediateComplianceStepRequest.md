# IntermediateComplianceStepRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** | The label of the compliance step | 
**compliance_step_type_request** | **str** | . The available values are: FilterStepRequest, GroupByStepRequest, GroupFilterStepRequest, BranchStepRequest, CheckStepRequest, PercentCheckStepRequest | 

## Example

```python
from lusid.models.intermediate_compliance_step_request import IntermediateComplianceStepRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IntermediateComplianceStepRequest from a JSON string
intermediate_compliance_step_request_instance = IntermediateComplianceStepRequest.from_json(json)
# print the JSON string representation of the object
print IntermediateComplianceStepRequest.to_json()

# convert the object into a dict
intermediate_compliance_step_request_dict = intermediate_compliance_step_request_instance.to_dict()
# create an instance of IntermediateComplianceStepRequest from a dict
intermediate_compliance_step_request_form_dict = intermediate_compliance_step_request.from_dict(intermediate_compliance_step_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


