# ComplianceStep


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**compliance_step_type** | **str** | . The available values are: FilterStep, GroupByStep, GroupFilterStep, BranchStep, RecombineStep, CheckStep, PercentCheckStep | 

## Example

```python
from lusid.models.compliance_step import ComplianceStep

# TODO update the JSON string below
json = "{}"
# create an instance of ComplianceStep from a JSON string
compliance_step_instance = ComplianceStep.from_json(json)
# print the JSON string representation of the object
print ComplianceStep.to_json()

# convert the object into a dict
compliance_step_dict = compliance_step_instance.to_dict()
# create an instance of ComplianceStep from a dict
compliance_step_form_dict = compliance_step.from_dict(compliance_step_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


