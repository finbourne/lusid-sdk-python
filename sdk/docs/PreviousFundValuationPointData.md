# PreviousFundValuationPointData

The data for a Fund at the previous valuation point.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nav** | [**FundPreviousNAV**](FundPreviousNAV.md) |  | 
**unitisation** | [**UnitisationData**](UnitisationData.md) |  | [optional] 

## Example

```python
from lusid.models.previous_fund_valuation_point_data import PreviousFundValuationPointData

# TODO update the JSON string below
json = "{}"
# create an instance of PreviousFundValuationPointData from a JSON string
previous_fund_valuation_point_data_instance = PreviousFundValuationPointData.from_json(json)
# print the JSON string representation of the object
print PreviousFundValuationPointData.to_json()

# convert the object into a dict
previous_fund_valuation_point_data_dict = previous_fund_valuation_point_data_instance.to_dict()
# create an instance of PreviousFundValuationPointData from a dict
previous_fund_valuation_point_data_form_dict = previous_fund_valuation_point_data.from_dict(previous_fund_valuation_point_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


