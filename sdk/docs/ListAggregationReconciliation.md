# ListAggregationReconciliation


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**left** | [**ListAggregationResponse**](ListAggregationResponse.md) |  | [optional] 
**right** | [**ListAggregationResponse**](ListAggregationResponse.md) |  | [optional] 
**diff** | **List[Dict[str, object]]** |  | [optional] 
**data_schema** | [**ResultDataSchema**](ResultDataSchema.md) |  | [optional] 

## Example

```python
from lusid.models.list_aggregation_reconciliation import ListAggregationReconciliation

# TODO update the JSON string below
json = "{}"
# create an instance of ListAggregationReconciliation from a JSON string
list_aggregation_reconciliation_instance = ListAggregationReconciliation.from_json(json)
# print the JSON string representation of the object
print ListAggregationReconciliation.to_json()

# convert the object into a dict
list_aggregation_reconciliation_dict = list_aggregation_reconciliation_instance.to_dict()
# create an instance of ListAggregationReconciliation from a dict
list_aggregation_reconciliation_form_dict = list_aggregation_reconciliation.from_dict(list_aggregation_reconciliation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


