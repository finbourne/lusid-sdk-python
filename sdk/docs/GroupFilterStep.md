# GroupFilterStep


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** | The label of the compliance step | 
**grouped_parameters** | **Dict[str, List[ComplianceTemplateParameter]]** | Parameters required for the step. Some step types group parameters to differentiate between, for example, hard limit and warning threshold parameters | 
**compliance_step_type** | **str** | . The available values are: FilterStep, GroupByStep, GroupFilterStep, BranchStep, RecombineStep | 

## Example

```python
from lusid.models.group_filter_step import GroupFilterStep

# TODO update the JSON string below
json = "{}"
# create an instance of GroupFilterStep from a JSON string
group_filter_step_instance = GroupFilterStep.from_json(json)
# print the JSON string representation of the object
print GroupFilterStep.to_json()

# convert the object into a dict
group_filter_step_dict = group_filter_step_instance.to_dict()
# create an instance of GroupFilterStep from a dict
group_filter_step_form_dict = group_filter_step.from_dict(group_filter_step_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

