# Quote

The quote id, value and lineage of the quotes all keyed by a unique correlation id.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quote_id** | [**QuoteId**](QuoteId.md) |  | 
**metric_value** | [**MetricValue**](MetricValue.md) |  | [optional] 
**lineage** | **str** | Description of the quote&#39;s lineage e.g. &#39;FundAccountant_GreenQuality&#39;. | [optional] 
**cut_label** | **str** | The cut label that this quote was updated or inserted with. | [optional] 
**uploaded_by** | **str** | The unique id of the user that updated or inserted the quote. | 
**as_at** | **datetime** | The asAt datetime at which the quote was committed to LUSID. | 
**scale_factor** | **float** | An optional scale factor for non-standard scaling of quotes against the instrument. For example, if you wish the quote&#39;s Value to be scaled down by a factor of 100, enter 100. If not supplied, the default ScaleFactor is 1. | [optional] 

## Example

```python
from lusid.models.quote import Quote

# TODO update the JSON string below
json = "{}"
# create an instance of Quote from a JSON string
quote_instance = Quote.from_json(json)
# print the JSON string representation of the object
print Quote.to_json()

# convert the object into a dict
quote_dict = quote_instance.to_dict()
# create an instance of Quote from a dict
quote_form_dict = quote.from_dict(quote_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


