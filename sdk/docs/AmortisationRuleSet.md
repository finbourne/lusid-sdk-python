# AmortisationRuleSet


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**id** | [**ResourceId**](ResourceId.md) |  | 
**display_name** | **str** | A user-friendly name. | 
**description** | **str** | A description of what this rule set is for. | [optional] 
**rules** | [**List[AmortisationRule]**](AmortisationRule.md) | The rules of this rule set. | 
**version** | [**Version**](Version.md) |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.amortisation_rule_set import AmortisationRuleSet

# TODO update the JSON string below
json = "{}"
# create an instance of AmortisationRuleSet from a JSON string
amortisation_rule_set_instance = AmortisationRuleSet.from_json(json)
# print the JSON string representation of the object
print AmortisationRuleSet.to_json()

# convert the object into a dict
amortisation_rule_set_dict = amortisation_rule_set_instance.to_dict()
# create an instance of AmortisationRuleSet from a dict
amortisation_rule_set_form_dict = amortisation_rule_set.from_dict(amortisation_rule_set_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


