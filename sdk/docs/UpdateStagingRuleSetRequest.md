# UpdateStagingRuleSetRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | The name of the staging rule set. | 
**description** | **str** | A description for the staging rule set. | [optional] 
**rules** | [**List[StagingRule]**](StagingRule.md) | The list of staging rules that apply to a specific entity type. | 

## Example

```python
from lusid.models.update_staging_rule_set_request import UpdateStagingRuleSetRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateStagingRuleSetRequest from a JSON string
update_staging_rule_set_request_instance = UpdateStagingRuleSetRequest.from_json(json)
# print the JSON string representation of the object
print UpdateStagingRuleSetRequest.to_json()

# convert the object into a dict
update_staging_rule_set_request_dict = update_staging_rule_set_request_instance.to_dict()
# create an instance of UpdateStagingRuleSetRequest from a dict
update_staging_rule_set_request_form_dict = update_staging_rule_set_request.from_dict(update_staging_rule_set_request_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


