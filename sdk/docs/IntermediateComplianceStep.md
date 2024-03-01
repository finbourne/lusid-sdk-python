# IntermediateComplianceStep


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** | The label of the compliance step | 
**grouped_parameters** | **Dict[str, List[ComplianceTemplateParameter]]** | Parameters required for the step | 
**compliance_step_type** | **str** | . The available values are: FilterStep, GroupByStep, GroupFilterStep, BranchStep, RecombineStep, CheckStep | 

## Example

```python
from lusid.models.intermediate_compliance_step import IntermediateComplianceStep

# TODO update the JSON string below
json = "{}"
# create an instance of IntermediateComplianceStep from a JSON string
intermediate_compliance_step_instance = IntermediateComplianceStep.from_json(json)
# print the JSON string representation of the object
print IntermediateComplianceStep.to_json()

# convert the object into a dict
intermediate_compliance_step_dict = intermediate_compliance_step_instance.to_dict()
# create an instance of IntermediateComplianceStep from a dict
intermediate_compliance_step_form_dict = intermediate_compliance_step.from_dict(intermediate_compliance_step_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


