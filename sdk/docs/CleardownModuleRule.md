# CleardownModuleRule

A Cleardown rule

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rule_id** | **str** | The identifier for the Cleardown Rule. | 
**general_ledger_account_code** | **str** | The account to post the residual P&amp;L to. | 
**rule_filter** | **str** | The filter syntax for the Cleardown Rule. See https://support.lusid.com/knowledgebase/article/KA-02140 for more information on filter syntax. | 

## Example

```python
from lusid.models.cleardown_module_rule import CleardownModuleRule

# TODO update the JSON string below
json = "{}"
# create an instance of CleardownModuleRule from a JSON string
cleardown_module_rule_instance = CleardownModuleRule.from_json(json)
# print the JSON string representation of the object
print CleardownModuleRule.to_json()

# convert the object into a dict
cleardown_module_rule_dict = cleardown_module_rule_instance.to_dict()
# create an instance of CleardownModuleRule from a dict
cleardown_module_rule_form_dict = cleardown_module_rule.from_dict(cleardown_module_rule_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


