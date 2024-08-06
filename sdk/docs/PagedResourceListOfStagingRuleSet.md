# PagedResourceListOfStagingRuleSet


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next_page** | **str** |  | [optional] 
**previous_page** | **str** |  | [optional] 
**values** | [**List[StagingRuleSet]**](StagingRuleSet.md) |  | 
**href** | **str** |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.paged_resource_list_of_staging_rule_set import PagedResourceListOfStagingRuleSet

# TODO update the JSON string below
json = "{}"
# create an instance of PagedResourceListOfStagingRuleSet from a JSON string
paged_resource_list_of_staging_rule_set_instance = PagedResourceListOfStagingRuleSet.from_json(json)
# print the JSON string representation of the object
print PagedResourceListOfStagingRuleSet.to_json()

# convert the object into a dict
paged_resource_list_of_staging_rule_set_dict = paged_resource_list_of_staging_rule_set_instance.to_dict()
# create an instance of PagedResourceListOfStagingRuleSet from a dict
paged_resource_list_of_staging_rule_set_form_dict = paged_resource_list_of_staging_rule_set.from_dict(paged_resource_list_of_staging_rule_set_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


