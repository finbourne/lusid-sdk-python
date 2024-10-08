# GroupReconciliationDatePair


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**effective_at** | **datetime** | The effective at date for the reconciliation | [optional] 
**as_at** | **datetime** | The as at date for the reconciliation | [optional] 

## Example

```python
from lusid.models.group_reconciliation_date_pair import GroupReconciliationDatePair

# TODO update the JSON string below
json = "{}"
# create an instance of GroupReconciliationDatePair from a JSON string
group_reconciliation_date_pair_instance = GroupReconciliationDatePair.from_json(json)
# print the JSON string representation of the object
print GroupReconciliationDatePair.to_json()

# convert the object into a dict
group_reconciliation_date_pair_dict = group_reconciliation_date_pair_instance.to_dict()
# create an instance of GroupReconciliationDatePair from a dict
group_reconciliation_date_pair_form_dict = group_reconciliation_date_pair.from_dict(group_reconciliation_date_pair_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


