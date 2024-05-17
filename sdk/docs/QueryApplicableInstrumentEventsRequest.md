# QueryApplicableInstrumentEventsRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**window_start** | **datetime** | The start date of the window. | 
**window_end** | **datetime** | The end date of the window. | 
**effective_at** | **datetime** | The Effective date that splits query window into two parts: factual period and forecast period | 
**portfolio_entity_ids** | [**List[PortfolioEntityId]**](PortfolioEntityId.md) | The set of portfolios and portfolio groups to which the instrument events must belong. | 
**forecasting_recipe_id** | [**ResourceId**](ResourceId.md) |  | 

## Example

```python
from lusid.models.query_applicable_instrument_events_request import QueryApplicableInstrumentEventsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of QueryApplicableInstrumentEventsRequest from a JSON string
query_applicable_instrument_events_request_instance = QueryApplicableInstrumentEventsRequest.from_json(json)
# print the JSON string representation of the object
print QueryApplicableInstrumentEventsRequest.to_json()

# convert the object into a dict
query_applicable_instrument_events_request_dict = query_applicable_instrument_events_request_instance.to_dict()
# create an instance of QueryApplicableInstrumentEventsRequest from a dict
query_applicable_instrument_events_request_form_dict = query_applicable_instrument_events_request.from_dict(query_applicable_instrument_events_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


