# ComplianceStepRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**compliance_step_type_request** | **str** | . The available values are: FilterStepRequest, GroupByStepRequest, GroupFilterStepRequest, BranchStepRequest, CheckStepRequest, PercentCheckStepRequest | 

## Example

```python
from lusid.models.compliance_step_request import ComplianceStepRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ComplianceStepRequest from a JSON string
compliance_step_request_instance = ComplianceStepRequest.from_json(json)
# print the JSON string representation of the object
print ComplianceStepRequest.to_json()

# convert the object into a dict
compliance_step_request_dict = compliance_step_request_instance.to_dict()
# create an instance of ComplianceStepRequest from a dict
compliance_step_request_form_dict = compliance_step_request.from_dict(compliance_step_request_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


