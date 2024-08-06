# StagingRuleApprovalCriteria


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**required_approvals** | **int** |  | [optional] 
**deciding_user** | **str** |  | [optional] 
**staging_user_can_decide** | **bool** |  | [optional] 

## Example

```python
from lusid.models.staging_rule_approval_criteria import StagingRuleApprovalCriteria

# TODO update the JSON string below
json = "{}"
# create an instance of StagingRuleApprovalCriteria from a JSON string
staging_rule_approval_criteria_instance = StagingRuleApprovalCriteria.from_json(json)
# print the JSON string representation of the object
print StagingRuleApprovalCriteria.to_json()

# convert the object into a dict
staging_rule_approval_criteria_dict = staging_rule_approval_criteria_instance.to_dict()
# create an instance of StagingRuleApprovalCriteria from a dict
staging_rule_approval_criteria_form_dict = staging_rule_approval_criteria.from_dict(staging_rule_approval_criteria_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


