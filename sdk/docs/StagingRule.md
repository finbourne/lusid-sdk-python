# StagingRule


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rule_id** | **str** | The ID of the staging rule. | 
**description** | **str** | A description for the staging rule. | [optional] 
**status** | **str** | Whether the rule is &#39;Active&#39; or &#39;Inactive&#39;. | 
**match_criteria** | [**StagingRuleMatchCriteria**](StagingRuleMatchCriteria.md) |  | 
**approval_criteria** | [**StagingRuleApprovalCriteria**](StagingRuleApprovalCriteria.md) |  | 

## Example

```python
from lusid.models.staging_rule import StagingRule

# TODO update the JSON string below
json = "{}"
# create an instance of StagingRule from a JSON string
staging_rule_instance = StagingRule.from_json(json)
# print the JSON string representation of the object
print StagingRule.to_json()

# convert the object into a dict
staging_rule_dict = staging_rule_instance.to_dict()
# create an instance of StagingRule from a dict
staging_rule_form_dict = staging_rule.from_dict(staging_rule_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


