# GroupReconciliationDefinitionCurrencies


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**left** | **str** | Currency for the left side of a reconciliation | 
**right** | **str** | Currency for the right side of a reconciliation | 

## Example

```python
from lusid.models.group_reconciliation_definition_currencies import GroupReconciliationDefinitionCurrencies

# TODO update the JSON string below
json = "{}"
# create an instance of GroupReconciliationDefinitionCurrencies from a JSON string
group_reconciliation_definition_currencies_instance = GroupReconciliationDefinitionCurrencies.from_json(json)
# print the JSON string representation of the object
print GroupReconciliationDefinitionCurrencies.to_json()

# convert the object into a dict
group_reconciliation_definition_currencies_dict = group_reconciliation_definition_currencies_instance.to_dict()
# create an instance of GroupReconciliationDefinitionCurrencies from a dict
group_reconciliation_definition_currencies_form_dict = group_reconciliation_definition_currencies.from_dict(group_reconciliation_definition_currencies_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


