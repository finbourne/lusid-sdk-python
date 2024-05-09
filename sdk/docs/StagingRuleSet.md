# StagingRuleSet


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_type** | **str** | The entity type the staging rule set applies to. | 
**staging_rule_set_id** | **str** | System generated unique id for the staging rule set. | 
**display_name** | **str** | The name of the staging rule set. | 
**description** | **str** | A description for the staging rule set. | [optional] 
**rules** | [**List[StagingRule]**](StagingRule.md) | The list of staging rules that apply to a specific entity type. | 
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**version** | [**Version**](Version.md) |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.staging_rule_set import StagingRuleSet

# TODO update the JSON string below
json = "{}"
# create an instance of StagingRuleSet from a JSON string
staging_rule_set_instance = StagingRuleSet.from_json(json)
# print the JSON string representation of the object
print StagingRuleSet.to_json()

# convert the object into a dict
staging_rule_set_dict = staging_rule_set_instance.to_dict()
# create an instance of StagingRuleSet from a dict
staging_rule_set_form_dict = staging_rule_set.from_dict(staging_rule_set_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


