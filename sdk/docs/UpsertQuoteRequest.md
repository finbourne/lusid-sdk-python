# UpsertQuoteRequest

The details of the quote including its unique identifier, value and lineage.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quote_id** | [**QuoteId**](QuoteId.md) |  | 
**metric_value** | [**MetricValue**](MetricValue.md) |  | [optional] 
**lineage** | **str** | Description of the quote&#39;s lineage e.g. &#39;FundAccountant_GreenQuality&#39;. | [optional] 
**scale_factor** | **float** | An optional scale factor for non-standard scaling of quotes against the instrument. For example, if you wish the quote&#39;s Value to be scaled down by a factor of 100, enter 100. If not supplied, the default ScaleFactor is 1. | [optional] 

## Example

```python
from lusid.models.upsert_quote_request import UpsertQuoteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpsertQuoteRequest from a JSON string
upsert_quote_request_instance = UpsertQuoteRequest.from_json(json)
# print the JSON string representation of the object
print UpsertQuoteRequest.to_json()

# convert the object into a dict
upsert_quote_request_dict = upsert_quote_request_instance.to_dict()
# create an instance of UpsertQuoteRequest from a dict
upsert_quote_request_form_dict = upsert_quote_request.from_dict(upsert_quote_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


