# TranslateTradeTicketRequest

A collection of instruments to translate, along with the target dialect to translate into.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tickets** | [**Dict[str, TradeTicket]**](TradeTicket.md) | The collection of trade tickets to translate.              Each trade ticket should be keyed by a unique correlation id. This id is ephemeral and is not stored by LUSID. It serves only as a way to easily identify each instrument in the response. | 
**dialect** | **str** | The target dialect that the given instruments should be translated to. | 
## Example

```python
from lusid.models.translate_trade_ticket_request import TranslateTradeTicketRequest
from typing import Any, Dict
from pydantic.v1 import BaseModel, Field, constr, validator

tickets: Dict[str, TradeTicket] = # Replace with your value
dialect: StrictStr = "example_dialect"
translate_trade_ticket_request_instance = TranslateTradeTicketRequest(tickets=tickets, dialect=dialect)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

