# CheckStep


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** | The label of the compliance step | 
**limit_check_parameters** | [**List[ComplianceTemplateParameter]**](ComplianceTemplateParameter.md) | Parameters required for an absolute limit check | 
**warning_check_parameters** | [**List[ComplianceTemplateParameter]**](ComplianceTemplateParameter.md) | Parameters required for a warning limit check | 
**compliance_step_type** | **str** | . The available values are: FilterStep, GroupByStep, GroupFilterStep, BranchStep, RecombineStep, CheckStep, PercentCheckStep | 

## Example

```python
from lusid.models.check_step import CheckStep

# TODO update the JSON string below
json = "{}"
# create an instance of CheckStep from a JSON string
check_step_instance = CheckStep.from_json(json)
# print the JSON string representation of the object
print CheckStep.to_json()

# convert the object into a dict
check_step_dict = check_step_instance.to_dict()
# create an instance of CheckStep from a dict
check_step_form_dict = check_step.from_dict(check_step_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


