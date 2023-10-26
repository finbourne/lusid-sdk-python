# TranslateTradeTicketsResponse

A response from a request to translate a collection of instruments to a given target dialect.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**values** | [**Dict[str, TradeTicket]**](TradeTicket.md) | The instruments which have been successfully translated. | [optional] 
**failed** | [**Dict[str, ErrorDetail]**](ErrorDetail.md) | The instruments that could not be translated along with a reason for their failure. | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.translate_trade_tickets_response import TranslateTradeTicketsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TranslateTradeTicketsResponse from a JSON string
translate_trade_tickets_response_instance = TranslateTradeTicketsResponse.from_json(json)
# print the JSON string representation of the object
print TranslateTradeTicketsResponse.to_json()

# convert the object into a dict
translate_trade_tickets_response_dict = translate_trade_tickets_response_instance.to_dict()
# create an instance of TranslateTradeTicketsResponse from a dict
translate_trade_tickets_response_form_dict = translate_trade_tickets_response.from_dict(translate_trade_tickets_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


