# AmortisationRule


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the rule. | 
**description** | **str** | A description of the rule. | [optional] 
**filter** | **str** | The filter for this rule. | 
**amortisation_method** | **str** | The filter for this rule. | 

## Example

```python
from lusid.models.amortisation_rule import AmortisationRule

# TODO update the JSON string below
json = "{}"
# create an instance of AmortisationRule from a JSON string
amortisation_rule_instance = AmortisationRule.from_json(json)
# print the JSON string representation of the object
print AmortisationRule.to_json()

# convert the object into a dict
amortisation_rule_dict = amortisation_rule_instance.to_dict()
# create an instance of AmortisationRule from a dict
amortisation_rule_form_dict = amortisation_rule.from_dict(amortisation_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


