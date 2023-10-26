# HoldingsAdjustment

Full content of a holdings adjustment for a single portfolio and effective date.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**effective_at** | **datetime** | The effective datetime from which the adjustment is valid. There can only be one holdings adjustment for a transaction portfolio at a specific effective datetime, so this uniquely identifies the adjustment. | 
**version** | [**Version**](Version.md) |  | 
**unmatched_holding_method** | **str** | Describes how the holdings were adjusted. If &#39;PositionToZero&#39; the entire transaction portfolio&#39;s holdings were set via a call to &#39;Set holdings&#39;. If &#39;KeepTheSame&#39; only the specified holdings were adjusted via a call to &#39;Adjust holdings&#39;. The available values are: PositionToZero, KeepTheSame | 
**adjustments** | [**List[HoldingAdjustment]**](HoldingAdjustment.md) | The holding adjustments. | 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid.models.holdings_adjustment import HoldingsAdjustment

# TODO update the JSON string below
json = "{}"
# create an instance of HoldingsAdjustment from a JSON string
holdings_adjustment_instance = HoldingsAdjustment.from_json(json)
# print the JSON string representation of the object
print HoldingsAdjustment.to_json()

# convert the object into a dict
holdings_adjustment_dict = holdings_adjustment_instance.to_dict()
# create an instance of HoldingsAdjustment from a dict
holdings_adjustment_form_dict = holdings_adjustment.from_dict(holdings_adjustment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


