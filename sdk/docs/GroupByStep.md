# GroupByStep


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** | The label of the compliance step | 
**parameters** | [**List[ComplianceTemplateParameter]**](ComplianceTemplateParameter.md) | Parameters required for the step | 
**compliance_step_type** | **str** | . The available values are: FilterStep, GroupByStep, GroupFilterStep, BranchStep, RecombineStep | 

## Example

```python
from lusid.models.group_by_step import GroupByStep

# TODO update the JSON string below
json = "{}"
# create an instance of GroupByStep from a JSON string
group_by_step_instance = GroupByStep.from_json(json)
# print the JSON string representation of the object
print GroupByStep.to_json()

# convert the object into a dict
group_by_step_dict = group_by_step_instance.to_dict()
# create an instance of GroupByStep from a dict
group_by_step_form_dict = group_by_step.from_dict(group_by_step_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


