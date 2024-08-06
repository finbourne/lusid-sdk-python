# PortfoliosReconciliationRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**left** | [**PortfolioReconciliationRequest**](PortfolioReconciliationRequest.md) |  | 
**right** | [**PortfolioReconciliationRequest**](PortfolioReconciliationRequest.md) |  | 
**instrument_property_keys** | **List[str]** | Instrument properties to be included with any identified breaks. These properties will be in the effective and AsAt dates of the left portfolio | 

## Example

```python
from lusid.models.portfolios_reconciliation_request import PortfoliosReconciliationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PortfoliosReconciliationRequest from a JSON string
portfolios_reconciliation_request_instance = PortfoliosReconciliationRequest.from_json(json)
# print the JSON string representation of the object
print PortfoliosReconciliationRequest.to_json()

# convert the object into a dict
portfolios_reconciliation_request_dict = portfolios_reconciliation_request_instance.to_dict()
# create an instance of PortfoliosReconciliationRequest from a dict
portfolios_reconciliation_request_form_dict = portfolios_reconciliation_request.from_dict(portfolios_reconciliation_request_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


