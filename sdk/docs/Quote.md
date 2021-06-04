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
**scale_factor** | **float** | An optional scale factor for non-standard scaling of quotes against the instrument. If not supplied, the default ScaleFactor is 1. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


