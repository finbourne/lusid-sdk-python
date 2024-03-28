# CreateStagingRuleSetRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | The name of the staging rule set. | [optional] 
**description** | **str** | A description for the staging rule set. | [optional] 
**rules** | [**List[StagingRule]**](StagingRule.md) | The list of staging rules that apply to a specific entity type. | 

## Example

```python
from lusid.models.create_staging_rule_set_request import CreateStagingRuleSetRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateStagingRuleSetRequest from a JSON string
create_staging_rule_set_request_instance = CreateStagingRuleSetRequest.from_json(json)
# print the JSON string representation of the object
print CreateStagingRuleSetRequest.to_json()

# convert the object into a dict
create_staging_rule_set_request_dict = create_staging_rule_set_request_instance.to_dict()
# create an instance of CreateStagingRuleSetRequest from a dict
create_staging_rule_set_request_form_dict = create_staging_rule_set_request.from_dict(create_staging_rule_set_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


