# PagedResourceListOfAmortisationRuleSet


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next_page** | **str** |  | [optional] 
**previous_page** | **str** |  | [optional] 
**values** | [**List[AmortisationRuleSet]**](AmortisationRuleSet.md) |  | 
**href** | **str** |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.paged_resource_list_of_amortisation_rule_set import PagedResourceListOfAmortisationRuleSet

# TODO update the JSON string below
json = "{}"
# create an instance of PagedResourceListOfAmortisationRuleSet from a JSON string
paged_resource_list_of_amortisation_rule_set_instance = PagedResourceListOfAmortisationRuleSet.from_json(json)
# print the JSON string representation of the object
print PagedResourceListOfAmortisationRuleSet.to_json()

# convert the object into a dict
paged_resource_list_of_amortisation_rule_set_dict = paged_resource_list_of_amortisation_rule_set_instance.to_dict()
# create an instance of PagedResourceListOfAmortisationRuleSet from a dict
paged_resource_list_of_amortisation_rule_set_form_dict = paged_resource_list_of_amortisation_rule_set.from_dict(paged_resource_list_of_amortisation_rule_set_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


