# GroupReconciliationAggregateAttributeValues


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**left_aggregate_attributes** | [**List[ComparisonAttributeValuePair]**](ComparisonAttributeValuePair.md) | Aggregate attribute names and values for the left hand entity being reconciled. | 
**right_aggregate_attributes** | [**List[ComparisonAttributeValuePair]**](ComparisonAttributeValuePair.md) | Aggregate attribute names and values for the right hand entity being reconciled. | 

## Example

```python
from lusid.models.group_reconciliation_aggregate_attribute_values import GroupReconciliationAggregateAttributeValues

# TODO update the JSON string below
json = "{}"
# create an instance of GroupReconciliationAggregateAttributeValues from a JSON string
group_reconciliation_aggregate_attribute_values_instance = GroupReconciliationAggregateAttributeValues.from_json(json)
# print the JSON string representation of the object
print GroupReconciliationAggregateAttributeValues.to_json()

# convert the object into a dict
group_reconciliation_aggregate_attribute_values_dict = group_reconciliation_aggregate_attribute_values_instance.to_dict()
# create an instance of GroupReconciliationAggregateAttributeValues from a dict
group_reconciliation_aggregate_attribute_values_form_dict = group_reconciliation_aggregate_attribute_values.from_dict(group_reconciliation_aggregate_attribute_values_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


