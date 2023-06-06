# ReconciliationRule

Base class for representing reconciliation rules in LUSID.  Reconciliation rules describe how a comparison between two items in the reconciliation should be performed and what constitutes equality.  This does not influence WHAT constitutes a match, but only whether once a line has been matched whether an item within it matches another item.  If a rule is not given for an item, it will default to equality comparison.  This base class should not be directly instantiated; each supported ReconciliationRuleType has a corresponding inherited class.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rule_type** | **str** | The available values are: ReconcileNumericRule, ReconcileDateTimeRule, ReconcileStringRule, ReconcileExact | 

## Example

```python
from lusid.models.reconciliation_rule import ReconciliationRule

# TODO update the JSON string below
json = "{}"
# create an instance of ReconciliationRule from a JSON string
reconciliation_rule_instance = ReconciliationRule.from_json(json)
# print the JSON string representation of the object
print ReconciliationRule.to_json()

# convert the object into a dict
reconciliation_rule_dict = reconciliation_rule_instance.to_dict()
# create an instance of ReconciliationRule from a dict
reconciliation_rule_form_dict = reconciliation_rule.from_dict(reconciliation_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


