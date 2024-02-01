# PostingModuleRule

A Posting rule

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rule_id** | **str** | The identifier for the Posting Rule. | 
**account** | **str** | The general ledger account to post the Activity credit or debit to. | [optional] 
**rule_filter** | **str** | The filter syntax for the Posting Rule. See https://support.lusid.com/knowledgebase/article/KA-02140 for more information on filter syntax. | 
**general_ledger_account_code** | **str** | The general ledger account to post the Activity credit or debit to. | [optional] 

## Example

```python
from lusid.models.posting_module_rule import PostingModuleRule

# TODO update the JSON string below
json = "{}"
# create an instance of PostingModuleRule from a JSON string
posting_module_rule_instance = PostingModuleRule.from_json(json)
# print the JSON string representation of the object
print PostingModuleRule.to_json()

# convert the object into a dict
posting_module_rule_dict = posting_module_rule_instance.to_dict()
# create an instance of PostingModuleRule from a dict
posting_module_rule_form_dict = posting_module_rule.from_dict(posting_module_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


