# BucketedCashFlowRequest

Specification class consisting of parameters for BucketedCashFlow endpoint.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rounding_method** | **str** | When bucketing, there is not a unique way to allocate the bucket points.  RoundingMethod Supported string (enumeration) values are: [RoundDown, RoundUp]. | 
**bucketing_dates** | **List[datetime]** | A list of dates to perform cashflow bucketing upon.  If this is provided, the list of tenors for bucketing should be empty. | [optional] 
**bucket_tenors** | **List[str]** | A list of tenors to perform cashflow bucketing upon.  If this is provided, the list of dates for bucketing should be empty. | [optional] 
**effective_at** | **str** | The valuation (pricing) effective datetime or cut label (inclusive) at which to evaluate the cashflows.  This determines whether cashflows are evaluated in a historic or forward looking context and will, for certain models, affect where data is looked up.  For example, on a swap if the effectiveAt is in the middle of the window, cashflows before it will be historic and resets assumed to exist where if the effectiveAt  is before the start of the range they are forward looking and will be expectations assuming the model supports that.  There is evidently a presumption here about availability of data and that the effectiveAt is realistically on or before the real-world today. | [optional] 
**window_start** | **str** | The lower bound effective datetime or cut label (inclusive) from which to retrieve the cashflows.  There is no lower bound if this is not specified. | [optional] 
**window_end** | **str** | The upper bound effective datetime or cut label (inclusive) from which to retrieve the cashflows.  The upper bound defaults to &#39;today&#39; if it is not specified | [optional] 
**recipe_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**report_currency** | **str** | Three letter ISO currency string indicating what currency to report in for ReportCurrency denominated queries. | [optional] 
**group_by** | **List[str]** | The set of items by which to perform grouping. This primarily matters when one or more of the metric operators is a mapping  that reduces set size, e.g. sum or proportion. The group-by statement determines the set of keys by which to break the results out. | [optional] 
**addresses** | **List[str]** | The set of items that the user wishes to see in the results. If empty, will be defaulted to standard ones. | [optional] 
**equip_with_subtotals** | **bool** | Flag directing the Valuation call to populate the results with subtotals of aggregates. | [optional] 
**as_at** | **datetime** | The time of the system at which to query for bucketed cashflows. | [optional] 
**exclude_unsettled_trades** | **bool** | Flag directing the Valuation call to exclude cashflows from unsettled trades.  If absent or set to false, cashflows will returned based on trade date - more specifically, cashflows from any unsettled trades will be included in the results. If set to true, unsettled trades will be excluded from the result set. | [optional] 
**cash_flow_type** | **str** | Indicate the requested cash flow representation InstrumentCashFlows or PortfolioCashFlows (GetCashLadder uses this)  Options: [InstrumentCashFlow, PortfolioCashFlow] | [optional] 
**bucketing_schedule** | [**BucketingSchedule**](BucketingSchedule.md) |  | [optional] 
**filter** | **str** |  | [optional] 

## Example

```python
from lusid.models.bucketed_cash_flow_request import BucketedCashFlowRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BucketedCashFlowRequest from a JSON string
bucketed_cash_flow_request_instance = BucketedCashFlowRequest.from_json(json)
# print the JSON string representation of the object
print BucketedCashFlowRequest.to_json()

# convert the object into a dict
bucketed_cash_flow_request_dict = bucketed_cash_flow_request_instance.to_dict()
# create an instance of BucketedCashFlowRequest from a dict
bucketed_cash_flow_request_form_dict = bucketed_cash_flow_request.from_dict(bucketed_cash_flow_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


