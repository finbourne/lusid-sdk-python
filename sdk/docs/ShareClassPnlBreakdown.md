# ShareClassPnlBreakdown

The breakdown of PnL for a Share Class on a specified date.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apportioned_non_class_specific_pnl** | [**Dict[str, ShareClassAmount]**](ShareClassAmount.md) | Bucket of detail for PnL within the queried period not explicitly allocated to any share class but has been apportioned to the share class. | 
**class_pnl** | [**Dict[str, ShareClassAmount]**](ShareClassAmount.md) | Bucket of detail for PnL specific to the share class within the queried period. | 
**total_pnl** | [**Dict[str, ShareClassAmount]**](ShareClassAmount.md) | Bucket of detail for the sum of class PnL and PnL not specific to a class within the queried period. | 

## Example

```python
from lusid.models.share_class_pnl_breakdown import ShareClassPnlBreakdown

# TODO update the JSON string below
json = "{}"
# create an instance of ShareClassPnlBreakdown from a JSON string
share_class_pnl_breakdown_instance = ShareClassPnlBreakdown.from_json(json)
# print the JSON string representation of the object
print ShareClassPnlBreakdown.to_json()

# convert the object into a dict
share_class_pnl_breakdown_dict = share_class_pnl_breakdown_instance.to_dict()
# create an instance of ShareClassPnlBreakdown from a dict
share_class_pnl_breakdown_form_dict = share_class_pnl_breakdown.from_dict(share_class_pnl_breakdown_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


