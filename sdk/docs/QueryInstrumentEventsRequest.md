# QueryInstrumentEventsRequest

Instrument event query.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**as_at** | **datetime** | The time of the system at which to query for bucketed cashflows. | [optional] 
**window_start** | **datetime** | The start date of the window. | 
**window_end** | **datetime** | The end date of the window. | 
**portfolio_entity_ids** | [**List[PortfolioEntityId]**](PortfolioEntityId.md) | The set of portfolios and portfolio groups to which the instrument events must belong. | 
**effective_at** | **datetime** | The Effective date used in the valuation of the cashflows. | 
**recipe_id** | [**ResourceId**](ResourceId.md) |  | 
**filter_instrument_events** | **str** | Expression to filter the result set. | [optional] 

## Example

```python
from lusid.models.query_instrument_events_request import QueryInstrumentEventsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of QueryInstrumentEventsRequest from a JSON string
query_instrument_events_request_instance = QueryInstrumentEventsRequest.from_json(json)
# print the JSON string representation of the object
print QueryInstrumentEventsRequest.to_json()

# convert the object into a dict
query_instrument_events_request_dict = query_instrument_events_request_instance.to_dict()
# create an instance of QueryInstrumentEventsRequest from a dict
query_instrument_events_request_form_dict = query_instrument_events_request.from_dict(query_instrument_events_request_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


