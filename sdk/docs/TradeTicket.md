# TradeTicket

The base class for representing a Trade Ticket in LUSID.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**trade_ticket_type** | **str** | The available values are: LusidTradeTicket, ExternalTradeTicket | 

## Example

```python
from lusid.models.trade_ticket import TradeTicket

# TODO update the JSON string below
json = "{}"
# create an instance of TradeTicket from a JSON string
trade_ticket_instance = TradeTicket.from_json(json)
# print the JSON string representation of the object
print TradeTicket.to_json()

# convert the object into a dict
trade_ticket_dict = trade_ticket_instance.to_dict()
# create an instance of TradeTicket from a dict
trade_ticket_form_dict = trade_ticket.from_dict(trade_ticket_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


