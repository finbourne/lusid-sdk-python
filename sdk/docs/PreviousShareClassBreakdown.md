# PreviousShareClassBreakdown

The data for a Share Class at the previous valuation point.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nav** | [**PreviousNAV**](PreviousNAV.md) |  | 
**unitisation** | [**UnitisationData**](UnitisationData.md) |  | [optional] 
**share_class_to_fund_fx_rate** | **float** | The fx rate from the Share Class currency to the fund currency at this valuation point. | 

## Example

```python
from lusid.models.previous_share_class_breakdown import PreviousShareClassBreakdown

# TODO update the JSON string below
json = "{}"
# create an instance of PreviousShareClassBreakdown from a JSON string
previous_share_class_breakdown_instance = PreviousShareClassBreakdown.from_json(json)
# print the JSON string representation of the object
print PreviousShareClassBreakdown.to_json()

# convert the object into a dict
previous_share_class_breakdown_dict = previous_share_class_breakdown_instance.to_dict()
# create an instance of PreviousShareClassBreakdown from a dict
previous_share_class_breakdown_form_dict = previous_share_class_breakdown.from_dict(previous_share_class_breakdown_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


