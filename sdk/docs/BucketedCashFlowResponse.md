# BucketedCashFlowResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** |  | [optional] 
**data** | **List[Dict[str, object]]** | List of dictionary bucketed cash flow result set.  Each dictionary represent a bucketed cashflow result set keyed by AddressKeys.  e.g. dictionary[\&quot;Valuation/CashFlowAmount\&quot;] for the aggregated cash flow amount for the bucket.  e.g. suppose \&quot;RoundUp\&quot; method, then dictionary[\&quot;Valuation/CashFlowDate/RoundUp\&quot;] returns the bucketed cashflow date. | [optional] 
**report_currency** | **str** | Three letter ISO currency string indicating what currency to report in for ReportCcy denominated queries.  If not present then the currency of the relevant portfolio will be used in its place where relevant. | [optional] 
**data_schema** | [**ResultDataSchema**](ResultDataSchema.md) |  | [optional] 
**failed** | [**Dict[str, ErrorDetail]**](ErrorDetail.md) | Information about where instruments have failed to return cashflows in so far as it is available.  e.g., failure to retrieve a market quote for a floating rate instrument. | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.bucketed_cash_flow_response import BucketedCashFlowResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BucketedCashFlowResponse from a JSON string
bucketed_cash_flow_response_instance = BucketedCashFlowResponse.from_json(json)
# print the JSON string representation of the object
print BucketedCashFlowResponse.to_json()

# convert the object into a dict
bucketed_cash_flow_response_dict = bucketed_cash_flow_response_instance.to_dict()
# create an instance of BucketedCashFlowResponse from a dict
bucketed_cash_flow_response_form_dict = bucketed_cash_flow_response.from_dict(bucketed_cash_flow_response_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


