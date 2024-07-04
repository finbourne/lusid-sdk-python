# FilterStep


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** | The label of the compliance step | 
**parameters** | [**List[ComplianceTemplateParameter]**](ComplianceTemplateParameter.md) | Parameters required for the step | 
**compliance_step_type** | **str** | . The available values are: FilterStep, GroupByStep, GroupFilterStep, BranchStep, RecombineStep, CheckStep, PercentCheckStep | 

## Example

```python
from lusid.models.filter_step import FilterStep

# TODO update the JSON string below
json = "{}"
# create an instance of FilterStep from a JSON string
filter_step_instance = FilterStep.from_json(json)
# print the JSON string representation of the object
print FilterStep.to_json()

# convert the object into a dict
filter_step_dict = filter_step_instance.to_dict()
# create an instance of FilterStep from a dict
filter_step_form_dict = filter_step.from_dict(filter_step_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


