# FundPnlBreakdown

The breakdown of PnL for a Fund on a specified date.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**non_class_specific_pnl** | [**Dict[str, FundAmount]**](FundAmount.md) | Bucket of detail for PnL within the queried period that is not specific to any share class. | 
**aggregated_class_pnl** | [**Dict[str, FundAmount]**](FundAmount.md) | Bucket of detail for the sum of class PnL across all share classes in a fund and within the queried period. | 
**total_pnl** | [**Dict[str, FundAmount]**](FundAmount.md) | Bucket of detail for the sum of class PnL and PnL not specific to a class within the queried period. | 

## Example

```python
from lusid.models.fund_pnl_breakdown import FundPnlBreakdown

# TODO update the JSON string below
json = "{}"
# create an instance of FundPnlBreakdown from a JSON string
fund_pnl_breakdown_instance = FundPnlBreakdown.from_json(json)
# print the JSON string representation of the object
print FundPnlBreakdown.to_json()

# convert the object into a dict
fund_pnl_breakdown_dict = fund_pnl_breakdown_instance.to_dict()
# create an instance of FundPnlBreakdown from a dict
fund_pnl_breakdown_form_dict = fund_pnl_breakdown.from_dict(fund_pnl_breakdown_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


