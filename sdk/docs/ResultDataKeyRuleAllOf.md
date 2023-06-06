# ResultDataKeyRuleAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**supplier** | **str** | the result resource supplier (where the data comes from) | 
**data_scope** | **str** | which is the scope in which the data should be found | 
**document_code** | **str** | document code that defines which document is desired | 
**quote_interval** | **str** | Shorthand for the time interval used to select result data. This must be a dot-separated string              specifying a start and end date, for example &#39;5D.0D&#39; to look back 5 days from today (0 days ago). | [optional] 
**as_at** | **datetime** | The AsAt predicate specification. | [optional] 
**resource_key** | **str** | The result data key that identifies the address pattern that this is a rule for | 
**document_result_type** | **str** |  | 
**result_key_rule_type** | **str** | The available values are: Invalid, ResultDataKeyRule, PortfolioResultDataKeyRule | 

## Example

```python
from lusid.models.result_data_key_rule_all_of import ResultDataKeyRuleAllOf

# TODO update the JSON string below
json = "{}"
# create an instance of ResultDataKeyRuleAllOf from a JSON string
result_data_key_rule_all_of_instance = ResultDataKeyRuleAllOf.from_json(json)
# print the JSON string representation of the object
print ResultDataKeyRuleAllOf.to_json()

# convert the object into a dict
result_data_key_rule_all_of_dict = result_data_key_rule_all_of_instance.to_dict()
# create an instance of ResultDataKeyRuleAllOf from a dict
result_data_key_rule_all_of_form_dict = result_data_key_rule_all_of.from_dict(result_data_key_rule_all_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


