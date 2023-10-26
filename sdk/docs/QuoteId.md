# QuoteId

The unique identifier of the quote.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quote_series_id** | [**QuoteSeriesId**](QuoteSeriesId.md) |  | 
**effective_at** | **str** | The effective datetime or cut label at which the quote is valid from. | 

## Example

```python
from lusid.models.quote_id import QuoteId

# TODO update the JSON string below
json = "{}"
# create an instance of QuoteId from a JSON string
quote_id_instance = QuoteId.from_json(json)
# print the JSON string representation of the object
print QuoteId.to_json()

# convert the object into a dict
quote_id_dict = quote_id_instance.to_dict()
# create an instance of QuoteId from a dict
quote_id_form_dict = quote_id.from_dict(quote_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


