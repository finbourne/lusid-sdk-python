# PortfolioReconciliationRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**portfolio_id** | [**ResourceId**](ResourceId.md) |  | 
**effective_at** | **str** | The effective date of the portfolio | 
**as_at** | **datetime** | Optional. The AsAt date of the portfolio | [optional] 

## Example

```python
from lusid.models.portfolio_reconciliation_request import PortfolioReconciliationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PortfolioReconciliationRequest from a JSON string
portfolio_reconciliation_request_instance = PortfolioReconciliationRequest.from_json(json)
# print the JSON string representation of the object
print PortfolioReconciliationRequest.to_json()

# convert the object into a dict
portfolio_reconciliation_request_dict = portfolio_reconciliation_request_instance.to_dict()
# create an instance of PortfolioReconciliationRequest from a dict
portfolio_reconciliation_request_form_dict = portfolio_reconciliation_request.from_dict(portfolio_reconciliation_request_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


