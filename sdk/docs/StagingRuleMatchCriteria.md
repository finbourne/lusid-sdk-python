# StagingRuleMatchCriteria


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action_in** | **List[str]** |  | [optional] 
**requesting_user** | **str** |  | [optional] 
**entity_attributes** | **str** |  | [optional] 
**changed_attribute_name_in** | **List[str]** |  | [optional] 

## Example

```python
from lusid.models.staging_rule_match_criteria import StagingRuleMatchCriteria

# TODO update the JSON string below
json = "{}"
# create an instance of StagingRuleMatchCriteria from a JSON string
staging_rule_match_criteria_instance = StagingRuleMatchCriteria.from_json(json)
# print the JSON string representation of the object
print StagingRuleMatchCriteria.to_json()

# convert the object into a dict
staging_rule_match_criteria_dict = staging_rule_match_criteria_instance.to_dict()
# create an instance of StagingRuleMatchCriteria from a dict
staging_rule_match_criteria_form_dict = staging_rule_match_criteria.from_dict(staging_rule_match_criteria_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


