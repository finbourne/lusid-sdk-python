# RecombineStep


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** | The label of the compliance step | 
**parameters** | [**List[ComplianceTemplateParameter]**](ComplianceTemplateParameter.md) | Parameters required for the step | 
**compliance_step_type** | **str** | . The available values are: FilterStep, GroupByStep, GroupFilterStep, BranchStep, RecombineStep | 

## Example

```python
from lusid.models.recombine_step import RecombineStep

# TODO update the JSON string below
json = "{}"
# create an instance of RecombineStep from a JSON string
recombine_step_instance = RecombineStep.from_json(json)
# print the JSON string representation of the object
print RecombineStep.to_json()

# convert the object into a dict
recombine_step_dict = recombine_step_instance.to_dict()
# create an instance of RecombineStep from a dict
recombine_step_form_dict = recombine_step.from_dict(recombine_step_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


