# ResultKeyRule

Base class for representing result key rules in LUSID, which describe how to resolve (unit) result data.  This base class should not be directly instantiated; each supported ResultKeyRuleType has a corresponding inherited class.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result_key_rule_type** | **str** | The available values are: Invalid, ResultDataKeyRule, PortfolioResultDataKeyRule | 

## Example

```python
from lusid.models.result_key_rule import ResultKeyRule

# TODO update the JSON string below
json = "{}"
# create an instance of ResultKeyRule from a JSON string
result_key_rule_instance = ResultKeyRule.from_json(json)
# print the JSON string representation of the object
print ResultKeyRule.to_json()

# convert the object into a dict
result_key_rule_dict = result_key_rule_instance.to_dict()
# create an instance of ResultKeyRule from a dict
result_key_rule_form_dict = result_key_rule.from_dict(result_key_rule_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


