# QueryTradeTicketsRequest

Query for tradetickets resulting from events on instrument that are taken from one or more portfolios

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**as_at** | **datetime** | The time of the system at which to query for tradetickets. | [optional] 
**window_start** | **datetime** | The start date of the window. | 
**window_end** | **datetime** | The end date of the window. | 
**portfolio_entity_ids** | [**List[PortfolioEntityId]**](PortfolioEntityId.md) | The set of portfolios and portfolio groups to which the instrument events must belong. | 
**recipe_id** | [**ResourceId**](ResourceId.md) |  | 
**effective_at** | **datetime** | The Effective date used in the valuation of the tradetickets. | 

## Example

```python
from lusid.models.query_trade_tickets_request import QueryTradeTicketsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of QueryTradeTicketsRequest from a JSON string
query_trade_tickets_request_instance = QueryTradeTicketsRequest.from_json(json)
# print the JSON string representation of the object
print QueryTradeTicketsRequest.to_json()

# convert the object into a dict
query_trade_tickets_request_dict = query_trade_tickets_request_instance.to_dict()
# create an instance of QueryTradeTicketsRequest from a dict
query_trade_tickets_request_form_dict = query_trade_tickets_request.from_dict(query_trade_tickets_request_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


