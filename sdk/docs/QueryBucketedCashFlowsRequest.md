# QueryBucketedCashFlowsRequest

Query for bucketed cashflows from one or more portfolios.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**as_at** | **datetime** | The time of the system at which to query for bucketed cashflows. | [optional] 
**window_start** | **datetime** | The start date of the window. | 
**window_end** | **datetime** | The end date of the window. | 
**portfolio_entity_ids** | [**List[PortfolioEntityId]**](PortfolioEntityId.md) | The set of portfolios and portfolio groups to which the instrument events must belong. | 
**effective_at** | **datetime** | The valuation (pricing) effective datetime or cut label (inclusive) at which to evaluate the cashflows | 
**recipe_id** | [**ResourceId**](ResourceId.md) |  | 
**rounding_method** | **str** | When bucketing, there is not a unique way to allocate the bucket points. RoundingMethod Supported string (enumeration) values are: [RoundDown, RoundUp]. | 
**bucketing_dates** | **List[datetime]** | A list of dates to perform cashflow bucketing upon. If this is provided, the list of tenors for bucketing should be empty. | [optional] 
**bucketing_tenors** | **List[str]** | A list of tenors to perform cashflow bucketing upon. If this is provided, the list of dates for bucketing should be empty. | [optional] 
**report_currency** | **str** | Three letter ISO currency string indicating what currency to report in for ReportCurrency denominated queries. | 
**group_by** | **List[str]** | The set of address keys to use to group the bucketed cash flows. | [optional] 
**addresses** | **List[str]** | The set of items that the user wishes to see in the results. If empty, will be defaulted to standard ones. | [optional] 
**equip_with_subtotals** | **bool** | Flag directing the Valuation call to populate the results with subtotals of aggregates. | [optional] 

## Example

```python
from lusid.models.query_bucketed_cash_flows_request import QueryBucketedCashFlowsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of QueryBucketedCashFlowsRequest from a JSON string
query_bucketed_cash_flows_request_instance = QueryBucketedCashFlowsRequest.from_json(json)
# print the JSON string representation of the object
print QueryBucketedCashFlowsRequest.to_json()

# convert the object into a dict
query_bucketed_cash_flows_request_dict = query_bucketed_cash_flows_request_instance.to_dict()
# create an instance of QueryBucketedCashFlowsRequest from a dict
query_bucketed_cash_flows_request_form_dict = query_bucketed_cash_flows_request.from_dict(query_bucketed_cash_flows_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


