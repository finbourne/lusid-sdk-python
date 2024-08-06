# CreateReconciliationRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | The unique identifier associated with the reconciliation | 
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
from lusid.models.create_reconciliation_request import CreateReconciliationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateReconciliationRequest from a JSON string
create_reconciliation_request_instance = CreateReconciliationRequest.from_json(json)
# print the JSON string representation of the object
print CreateReconciliationRequest.to_json()

# convert the object into a dict
create_reconciliation_request_dict = create_reconciliation_request_instance.to_dict()
# create an instance of CreateReconciliationRequest from a dict
create_reconciliation_request_form_dict = create_reconciliation_request.from_dict(create_reconciliation_request_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


