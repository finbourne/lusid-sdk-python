# GroupReconciliationCoreAttributeValues


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**left_core_attributes** | [**List[ComparisonAttributeValuePair]**](ComparisonAttributeValuePair.md) | Core attribute names and values for the left hand entity being reconciled. | 
**right_core_attributes** | [**List[ComparisonAttributeValuePair]**](ComparisonAttributeValuePair.md) | Core attribute names and values for the right hand entity being reconciled. | 

## Example

```python
from lusid.models.group_reconciliation_core_attribute_values import GroupReconciliationCoreAttributeValues

# TODO update the JSON string below
json = "{}"
# create an instance of GroupReconciliationCoreAttributeValues from a JSON string
group_reconciliation_core_attribute_values_instance = GroupReconciliationCoreAttributeValues.from_json(json)
# print the JSON string representation of the object
print GroupReconciliationCoreAttributeValues.to_json()

# convert the object into a dict
group_reconciliation_core_attribute_values_dict = group_reconciliation_core_attribute_values_instance.to_dict()
# create an instance of GroupReconciliationCoreAttributeValues from a dict
group_reconciliation_core_attribute_values_form_dict = group_reconciliation_core_attribute_values.from_dict(group_reconciliation_core_attribute_values_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


