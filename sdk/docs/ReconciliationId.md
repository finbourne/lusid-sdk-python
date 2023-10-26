# ReconciliationId


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scope** | [**DataScope**](DataScope.md) |  | [optional] 
**identifier** | **str** |  | [optional] 

## Example

```python
from lusid.models.reconciliation_id import ReconciliationId

# TODO update the JSON string below
json = "{}"
# create an instance of ReconciliationId from a JSON string
reconciliation_id_instance = ReconciliationId.from_json(json)
# print the JSON string representation of the object
print ReconciliationId.to_json()

# convert the object into a dict
reconciliation_id_dict = reconciliation_id_instance.to_dict()
# create an instance of ReconciliationId from a dict
reconciliation_id_form_dict = reconciliation_id.from_dict(reconciliation_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


