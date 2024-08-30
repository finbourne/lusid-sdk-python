# GroupReconciliationComparisonRuleStringValueMap


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**left_value** | **str** | The left string to map | 
**right_value** | **str** | The right string to map | 
**direction** | **str** | The direction to map. \&quot;UniDirectional\&quot; | \&quot;BiDirectional\&quot; | 

## Example

```python
from lusid.models.group_reconciliation_comparison_rule_string_value_map import GroupReconciliationComparisonRuleStringValueMap

# TODO update the JSON string below
json = "{}"
# create an instance of GroupReconciliationComparisonRuleStringValueMap from a JSON string
group_reconciliation_comparison_rule_string_value_map_instance = GroupReconciliationComparisonRuleStringValueMap.from_json(json)
# print the JSON string representation of the object
print GroupReconciliationComparisonRuleStringValueMap.to_json()

# convert the object into a dict
group_reconciliation_comparison_rule_string_value_map_dict = group_reconciliation_comparison_rule_string_value_map_instance.to_dict()
# create an instance of GroupReconciliationComparisonRuleStringValueMap from a dict
group_reconciliation_comparison_rule_string_value_map_form_dict = group_reconciliation_comparison_rule_string_value_map.from_dict(group_reconciliation_comparison_rule_string_value_map_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


