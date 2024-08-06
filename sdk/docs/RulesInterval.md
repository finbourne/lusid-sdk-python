# RulesInterval


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**effective_range** | [**DateRange**](DateRange.md) |  | 
**rules** | [**List[AmortisationRule]**](AmortisationRule.md) | The rules of this rule set. | 

## Example

```python
from lusid.models.rules_interval import RulesInterval

# TODO update the JSON string below
json = "{}"
# create an instance of RulesInterval from a JSON string
rules_interval_instance = RulesInterval.from_json(json)
# print the JSON string representation of the object
print RulesInterval.to_json()

# convert the object into a dict
rules_interval_dict = rules_interval_instance.to_dict()
# create an instance of RulesInterval from a dict
rules_interval_form_dict = rules_interval.from_dict(rules_interval_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


