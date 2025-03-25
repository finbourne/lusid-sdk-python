# ValuationPointDataResponse

The Valuation Point Data Response for the Fund and specified date.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**type** | **str** | The Type of the associated Diary Entry (&#39;PeriodBoundary&#39;,&#39;ValuationPoint&#39;,&#39;Other&#39; or &#39;Adhoc&#39; when a diary entry wasn&#39;t used). | 
**status** | **str** | The status of a Diary Entry of Type &#39;ValuationPoint&#39;. Defaults to &#39;Estimate&#39; when upserting a diary entry, moves to &#39;Candidate&#39; or &#39;Final&#39; when a ValuationPoint is accepted, and &#39;Final&#39; when it is finalised. The status of a Diary Entry becomes &#39;Unofficial&#39; when a diary entry wasn&#39;t used. | 
**fund_details** | [**FundDetails**](FundDetails.md) |  | 
**fund_valuation_point_data** | [**FundValuationPointData**](FundValuationPointData.md) |  | 
**share_class_data** | [**List[ShareClassData]**](ShareClassData.md) | The data for all share classes in fund. Share classes are identified by their short codes. | 
**valuation_point_code** | **str** | The code of the valuation point. | [optional] 
**previous_valuation_point_code** | **str** | The code of the previous valuation point. | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.valuation_point_data_response import ValuationPointDataResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ValuationPointDataResponse from a JSON string
valuation_point_data_response_instance = ValuationPointDataResponse.from_json(json)
# print the JSON string representation of the object
print ValuationPointDataResponse.to_json()

# convert the object into a dict
valuation_point_data_response_dict = valuation_point_data_response_instance.to_dict()
# create an instance of ValuationPointDataResponse from a dict
valuation_point_data_response_form_dict = valuation_point_data_response.from_dict(valuation_point_data_response_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


