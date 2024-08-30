# GroupReconciliationComparisonRuleTolerance


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of tolerance to allow. \&quot;Relative\&quot; | \&quot;Absolute\&quot; | 
**value** | **float** | The decimal value of how much tolerance to allow when comparing in relative (i.e percentage) or absolute terms depending on the ToleranceType specified | 

## Example

```python
from lusid.models.group_reconciliation_comparison_rule_tolerance import GroupReconciliationComparisonRuleTolerance

# TODO update the JSON string below
json = "{}"
# create an instance of GroupReconciliationComparisonRuleTolerance from a JSON string
group_reconciliation_comparison_rule_tolerance_instance = GroupReconciliationComparisonRuleTolerance.from_json(json)
# print the JSON string representation of the object
print GroupReconciliationComparisonRuleTolerance.to_json()

# convert the object into a dict
group_reconciliation_comparison_rule_tolerance_dict = group_reconciliation_comparison_rule_tolerance_instance.to_dict()
# create an instance of GroupReconciliationComparisonRuleTolerance from a dict
group_reconciliation_comparison_rule_tolerance_form_dict = group_reconciliation_comparison_rule_tolerance.from_dict(group_reconciliation_comparison_rule_tolerance_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


