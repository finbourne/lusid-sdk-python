# QueryCashFlowsRequest

Query for cashflows from one or more portfolios

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**as_at** | **datetime** | The time of the system at which to query for cashflows. | [optional] 
**window_start** | **datetime** | The start date of the window. | 
**window_end** | **datetime** | The end date of the window. | 
**portfolio_entity_ids** | [**List[PortfolioEntityId]**](PortfolioEntityId.md) | The set of portfolios and portfolio groups to which the instrument events must belong. | 
**recipe_id** | [**ResourceId**](ResourceId.md) |  | 
**effective_at** | **datetime** | The Effective date used in the valuation of the cashflows. | 

## Example

```python
from lusid.models.query_cash_flows_request import QueryCashFlowsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of QueryCashFlowsRequest from a JSON string
query_cash_flows_request_instance = QueryCashFlowsRequest.from_json(json)
# print the JSON string representation of the object
print QueryCashFlowsRequest.to_json()

# convert the object into a dict
query_cash_flows_request_dict = query_cash_flows_request_instance.to_dict()
# create an instance of QueryCashFlowsRequest from a dict
query_cash_flows_request_form_dict = query_cash_flows_request.from_dict(query_cash_flows_request_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


