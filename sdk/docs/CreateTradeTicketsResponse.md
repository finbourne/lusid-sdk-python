# CreateTradeTicketsResponse

Batch trade ticket creation response

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | [**List[LusidTradeTicket]**](LusidTradeTicket.md) |  | 
**failures** | [**List[ErrorDetail]**](ErrorDetail.md) |  | 

## Example

```python
from lusid.models.create_trade_tickets_response import CreateTradeTicketsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTradeTicketsResponse from a JSON string
create_trade_tickets_response_instance = CreateTradeTicketsResponse.from_json(json)
# print the JSON string representation of the object
print CreateTradeTicketsResponse.to_json()

# convert the object into a dict
create_trade_tickets_response_dict = create_trade_tickets_response_instance.to_dict()
# create an instance of CreateTradeTicketsResponse from a dict
create_trade_tickets_response_form_dict = create_trade_tickets_response.from_dict(create_trade_tickets_response_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


