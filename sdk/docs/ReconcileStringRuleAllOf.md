# ReconcileStringRuleAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comparison_type** | **str** | The available values are: Exact, Contains, CaseInsensitive, ContainsAnyCase, IsOneOf | 
**one_of_candidates** | **Dict[str, List[str]]** | For cases of \&quot;IsOneOf\&quot; a set is required to match values against.  Fuzzy matching of strings against one of a set. There can be cases where systems \&quot;A\&quot; and \&quot;B\&quot; might use different terms for the same logical entity. A common case would be  comparison of something like a day count fraction where some convention like the \&quot;actual 365\&quot; convention might be represented as one of [\&quot;A365\&quot;, \&quot;Act365\&quot;, \&quot;Actual365\&quot;] or similar.  This is to allow this kind of fuzzy matching of values. Note that as this is exhaustive comparison across sets it will be slow and should therefore be used sparingly. | [optional] 
**applies_to** | [**AggregateSpec**](AggregateSpec.md) |  | 
**rule_type** | **str** | The available values are: ReconcileNumericRule, ReconcileDateTimeRule, ReconcileStringRule, ReconcileExact | 

## Example

```python
from lusid.models.reconcile_string_rule_all_of import ReconcileStringRuleAllOf

# TODO update the JSON string below
json = "{}"
# create an instance of ReconcileStringRuleAllOf from a JSON string
reconcile_string_rule_all_of_instance = ReconcileStringRuleAllOf.from_json(json)
# print the JSON string representation of the object
print ReconcileStringRuleAllOf.to_json()

# convert the object into a dict
reconcile_string_rule_all_of_dict = reconcile_string_rule_all_of_instance.to_dict()
# create an instance of ReconcileStringRuleAllOf from a dict
reconcile_string_rule_all_of_form_dict = reconcile_string_rule_all_of.from_dict(reconcile_string_rule_all_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


