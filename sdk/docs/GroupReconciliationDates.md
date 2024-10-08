# GroupReconciliationDates


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**left** | [**GroupReconciliationDatePair**](GroupReconciliationDatePair.md) |  | [optional] 
**right** | [**GroupReconciliationDatePair**](GroupReconciliationDatePair.md) |  | [optional] 

## Example

```python
from lusid.models.group_reconciliation_dates import GroupReconciliationDates

# TODO update the JSON string below
json = "{}"
# create an instance of GroupReconciliationDates from a JSON string
group_reconciliation_dates_instance = GroupReconciliationDates.from_json(json)
# print the JSON string representation of the object
print GroupReconciliationDates.to_json()

# convert the object into a dict
group_reconciliation_dates_dict = group_reconciliation_dates_instance.to_dict()
# create an instance of GroupReconciliationDates from a dict
group_reconciliation_dates_form_dict = group_reconciliation_dates.from_dict(group_reconciliation_dates_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


