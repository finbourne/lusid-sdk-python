# UpdateReconciliationRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the scheduled reconciliation | [optional] 
**description** | **str** | A description of the scheduled reconciliation | [optional] 
**is_portfolio_group** | **bool** | Specifies whether reconciliation is between portfolios or portfolio groups | [optional] 
**left** | [**ResourceId**](ResourceId.md) |  | [optional] 
**right** | [**ResourceId**](ResourceId.md) |  | [optional] 
**transactions** | [**ReconciliationTransactions**](ReconciliationTransactions.md) |  | [optional] 
**positions** | [**ReconciliationConfiguration**](ReconciliationConfiguration.md) |  | [optional] 
**valuations** | [**ReconciliationConfiguration**](ReconciliationConfiguration.md) |  | [optional] 
**properties** | [**Dict[str, ModelProperty]**](ModelProperty.md) | Reconciliation properties | [optional] 

## Example

```python
from lusid.models.update_reconciliation_request import UpdateReconciliationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateReconciliationRequest from a JSON string
update_reconciliation_request_instance = UpdateReconciliationRequest.from_json(json)
# print the JSON string representation of the object
print UpdateReconciliationRequest.to_json()

# convert the object into a dict
update_reconciliation_request_dict = update_reconciliation_request_instance.to_dict()
# create an instance of UpdateReconciliationRequest from a dict
update_reconciliation_request_form_dict = update_reconciliation_request.from_dict(update_reconciliation_request_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


