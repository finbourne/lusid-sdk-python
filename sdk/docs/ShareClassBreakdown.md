# ShareClassBreakdown

The Valuation Point Data for a Share Class on a specified date.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**back_out** | [**Dict[str, ShareClassAmount]**](ShareClassAmount.md) | Bucket of detail for the Valuation Point where data points have been &#39;backed out&#39;. | 
**dealing** | [**ShareClassDealingBreakdown**](ShareClassDealingBreakdown.md) |  | 
**pn_l** | [**ShareClassPnlBreakdown**](ShareClassPnlBreakdown.md) |  | 
**gav** | [**ShareClassAmount**](ShareClassAmount.md) |  | 
**fees** | [**Dict[str, FeeAccrual]**](FeeAccrual.md) | Bucket of detail for any &#39;Fees&#39; that have been charged in the selected period. | 
**nav** | [**ShareClassAmount**](ShareClassAmount.md) |  | 
**unitisation** | [**UnitisationData**](UnitisationData.md) |  | [optional] 
**miscellaneous** | [**Dict[str, ShareClassAmount]**](ShareClassAmount.md) | Not used directly by the LUSID engines but serves as a holding area for any custom derived data points that may be useful in, for example, fee calculations). | [optional] 
**share_class_to_fund_fx_rate** | **float** | The fx rate from the Share Class currency to the fund currency at this valuation point. | 
**capital_ratio** | **float** | The proportion of the fund&#39;s adjusted beginning equity (ie: the sum of the previous NAV and the net dealing) that is invested in the share class. | 
**previous_share_class_breakdown** | [**PreviousShareClassBreakdown**](PreviousShareClassBreakdown.md) |  | 

## Example

```python
from lusid.models.share_class_breakdown import ShareClassBreakdown

# TODO update the JSON string below
json = "{}"
# create an instance of ShareClassBreakdown from a JSON string
share_class_breakdown_instance = ShareClassBreakdown.from_json(json)
# print the JSON string representation of the object
print ShareClassBreakdown.to_json()

# convert the object into a dict
share_class_breakdown_dict = share_class_breakdown_instance.to_dict()
# create an instance of ShareClassBreakdown from a dict
share_class_breakdown_form_dict = share_class_breakdown.from_dict(share_class_breakdown_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


