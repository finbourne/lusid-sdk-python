# FundValuationPointData

The Valuation Point Data for a Fund on a specified date.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**back_out** | [**Dict[str, FundAmount]**](FundAmount.md) | Bucket of detail for the Valuation Point where data points have been &#39;backed out&#39;. | 
**dealing** | [**Dict[str, FundAmount]**](FundAmount.md) | Bucket of detail for any &#39;Dealing&#39; that has occured inside the queried period. | 
**pn_l** | [**Dict[str, FundAmount]**](FundAmount.md) | Bucket of detail for &#39;PnL&#39; that has occured inside the queried period. | 
**gav** | **float** | The Gross Asset Value of the Fund or Share Class at the Valuation Point. This is effectively a summation of all Trial balance entries linked to accounts of types &#39;Asset&#39; and &#39;Liabilities&#39;. | 
**fees** | [**Dict[str, FeeAccrual]**](FeeAccrual.md) | Bucket of detail for any &#39;Fees&#39; that have been charged in the selected period. | 
**nav** | **float** | The Net Asset Value of the Fund or Share Class at the Valuation Point. This represents the GAV with any fees applied in the period. | 
**unitisation** | [**UnitisationData**](UnitisationData.md) |  | [optional] 
**miscellaneous** | [**Dict[str, FundAmount]**](FundAmount.md) | Not used directly by the LUSID engines but serves as a holding area for any custom derived data points that may be useful in, for example, fee calculations). | [optional] 
**previous_valuation_point_data** | [**PreviousFundValuationPointData**](PreviousFundValuationPointData.md) |  | [optional] 

## Example

```python
from lusid.models.fund_valuation_point_data import FundValuationPointData

# TODO update the JSON string below
json = "{}"
# create an instance of FundValuationPointData from a JSON string
fund_valuation_point_data_instance = FundValuationPointData.from_json(json)
# print the JSON string representation of the object
print FundValuationPointData.to_json()

# convert the object into a dict
fund_valuation_point_data_dict = fund_valuation_point_data_instance.to_dict()
# create an instance of FundValuationPointData from a dict
fund_valuation_point_data_form_dict = fund_valuation_point_data.from_dict(fund_valuation_point_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


