# ContributionToNonPassingRuleDetail


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rule_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**rule_status** | **str** | The status of the non-passing rule. | [optional] 
**breach_task_ids** | **List[str]** | The task ids associated with the compliance breach for this order&#39;s groups (if failing). | [optional] 
**likely_responsible_for_status** | **bool** | Whether this order is deemed as a likely contributor to the non-passing rule for this group. | [optional] 

## Example

```python
from lusid.models.contribution_to_non_passing_rule_detail import ContributionToNonPassingRuleDetail

# TODO update the JSON string below
json = "{}"
# create an instance of ContributionToNonPassingRuleDetail from a JSON string
contribution_to_non_passing_rule_detail_instance = ContributionToNonPassingRuleDetail.from_json(json)
# print the JSON string representation of the object
print ContributionToNonPassingRuleDetail.to_json()

# convert the object into a dict
contribution_to_non_passing_rule_detail_dict = contribution_to_non_passing_rule_detail_instance.to_dict()
# create an instance of ContributionToNonPassingRuleDetail from a dict
contribution_to_non_passing_rule_detail_form_dict = contribution_to_non_passing_rule_detail.from_dict(contribution_to_non_passing_rule_detail_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


