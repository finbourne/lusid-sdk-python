# ResourceListOfPortfolioTradeTicket


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | [**List[PortfolioTradeTicket]**](PortfolioTradeTicket.md) |  | 
**href** | **str** |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
**next_page** | **str** |  | [optional] 
**previous_page** | **str** |  | [optional] 

## Example

```python
from lusid.models.resource_list_of_portfolio_trade_ticket import ResourceListOfPortfolioTradeTicket

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceListOfPortfolioTradeTicket from a JSON string
resource_list_of_portfolio_trade_ticket_instance = ResourceListOfPortfolioTradeTicket.from_json(json)
# print the JSON string representation of the object
print ResourceListOfPortfolioTradeTicket.to_json()

# convert the object into a dict
resource_list_of_portfolio_trade_ticket_dict = resource_list_of_portfolio_trade_ticket_instance.to_dict()
# create an instance of ResourceListOfPortfolioTradeTicket from a dict
resource_list_of_portfolio_trade_ticket_form_dict = resource_list_of_portfolio_trade_ticket.from_dict(resource_list_of_portfolio_trade_ticket_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


