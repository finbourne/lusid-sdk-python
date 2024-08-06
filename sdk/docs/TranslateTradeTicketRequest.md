# TranslateTradeTicketRequest

A collection of instruments to translate, along with the target dialect to translate into.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tickets** | [**Dict[str, TradeTicket]**](TradeTicket.md) | The collection of trade tickets to translate.                Each trade ticket should be keyed by a unique correlation id. This id is ephemeral  and is not stored by LUSID. It serves only as a way to easily identify each instrument in the response. | 
**dialect** | **str** | The target dialect that the given instruments should be translated to. | 

## Example

```python
from lusid.models.translate_trade_ticket_request import TranslateTradeTicketRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TranslateTradeTicketRequest from a JSON string
translate_trade_ticket_request_instance = TranslateTradeTicketRequest.from_json(json)
# print the JSON string representation of the object
print TranslateTradeTicketRequest.to_json()

# convert the object into a dict
translate_trade_ticket_request_dict = translate_trade_ticket_request_instance.to_dict()
# create an instance of TranslateTradeTicketRequest from a dict
translate_trade_ticket_request_form_dict = translate_trade_ticket_request.from_dict(translate_trade_ticket_request_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


