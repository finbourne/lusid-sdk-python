# StagedModificationStagingRule


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**staging_rule_set_id** | **str** | System generated unique id for the staging rule set. | [optional] 
**rule_id** | **str** | The ID of the staging rule. | [optional] 
**required_approvals** | **int** | The number of approvals required. If left blank, one approval is needed. | [optional] 
**current_user_can_decide** | **bool** | True or False indicating whether the current user can make a decision on the staged modification. | [optional] 

## Example

```python
from lusid.models.staged_modification_staging_rule import StagedModificationStagingRule

# TODO update the JSON string below
json = "{}"
# create an instance of StagedModificationStagingRule from a JSON string
staged_modification_staging_rule_instance = StagedModificationStagingRule.from_json(json)
# print the JSON string representation of the object
print StagedModificationStagingRule.to_json()

# convert the object into a dict
staged_modification_staging_rule_dict = staged_modification_staging_rule_instance.to_dict()
# create an instance of StagedModificationStagingRule from a dict
staged_modification_staging_rule_form_dict = staged_modification_staging_rule.from_dict(staged_modification_staging_rule_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


