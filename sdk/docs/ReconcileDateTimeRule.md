# ReconcileDateTimeRule

Comparison of date time values

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comparison_type** | **str** | The available values are: Exact, AbsoluteDifference | 
**tolerance** | **float** | For a numeric type only (i.e. decimal, integer, date or datetime offset possibly controversially), this is the quantity used in the comparison.  The units of the tolerance must be set appropriately for the item being compared.  For a number such as a currency or amount that will be a simple quantity, for a DateTime or DateTimeOffset it should be days. If fewer than a single day then this should be  passed as a fraction. | [optional] 
**applies_to** | [**AggregateSpec**](AggregateSpec.md) |  | 
**rule_type** | **str** | The available values are: ReconcileNumericRule, ReconcileDateTimeRule, ReconcileStringRule, ReconcileExact | 

## Example

```python
from lusid.models.reconcile_date_time_rule import ReconcileDateTimeRule

# TODO update the JSON string below
json = "{}"
# create an instance of ReconcileDateTimeRule from a JSON string
reconcile_date_time_rule_instance = ReconcileDateTimeRule.from_json(json)
# print the JSON string representation of the object
print ReconcileDateTimeRule.to_json()

# convert the object into a dict
reconcile_date_time_rule_dict = reconcile_date_time_rule_instance.to_dict()
# create an instance of ReconcileDateTimeRule from a dict
reconcile_date_time_rule_form_dict = reconcile_date_time_rule.from_dict(reconcile_date_time_rule_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


