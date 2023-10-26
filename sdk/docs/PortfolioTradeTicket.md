# PortfolioTradeTicket

Response for querying trade tickets

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_portfolio_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**trade_ticket** | [**LusidTradeTicket**](LusidTradeTicket.md) |  | [optional] 

## Example

```python
from lusid.models.portfolio_trade_ticket import PortfolioTradeTicket

# TODO update the JSON string below
json = "{}"
# create an instance of PortfolioTradeTicket from a JSON string
portfolio_trade_ticket_instance = PortfolioTradeTicket.from_json(json)
# print the JSON string representation of the object
print PortfolioTradeTicket.to_json()

# convert the object into a dict
portfolio_trade_ticket_dict = portfolio_trade_ticket_instance.to_dict()
# create an instance of PortfolioTradeTicket from a dict
portfolio_trade_ticket_form_dict = portfolio_trade_ticket.from_dict(portfolio_trade_ticket_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


