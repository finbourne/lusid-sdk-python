# ModelSelection

The combination of a library to use and a model in that library that defines which pricing code will evaluate instruments  having a particular type/class. This allows us to control the model type and library for a given instrument.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**library** | **str** | The available values are: Lusid, RefinitivQps, RefinitivTracsWeb, VolMaster, IsdaCds, YieldBook, LusidCalc | 
**model** | **str** | The available values are: SimpleStatic, Discounting, VendorDefault, BlackScholes, ConstantTimeValueOfMoney, Bachelier, ForwardWithPoints, ForwardWithPointsUndiscounted, ForwardSpecifiedRate, ForwardSpecifiedRateUndiscounted, IndexNav, IndexPrice, InlinedIndex, ForwardFromCurve, ForwardFromCurveUndiscounted, BlackScholesDigital, BjerksundStensland1993, BondLookupPricer, FlexibleLoanPricer, CdsLookupPricer | 

## Example

```python
from lusid.models.model_selection import ModelSelection

# TODO update the JSON string below
json = "{}"
# create an instance of ModelSelection from a JSON string
model_selection_instance = ModelSelection.from_json(json)
# print the JSON string representation of the object
print ModelSelection.to_json()

# convert the object into a dict
model_selection_dict = model_selection_instance.to_dict()
# create an instance of ModelSelection from a dict
model_selection_form_dict = model_selection.from_dict(model_selection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


