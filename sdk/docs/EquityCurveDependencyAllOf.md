# EquityCurveDependencyAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**market_identifier** | **str** | Type of the code identifying the corresponding equity, e.g. ISIN or CUSIP | 
**code** | **str** | The code identifying the corresponding equity, e.g. US0378331005 if the MarketIdentifier was set to ISIN | 
**curve_type** | **str** | The curve type of the EquityCurve required. E.g. EquityCurveByPrices | 
**var_date** | **datetime** | The effectiveDate of the entity that this is a dependency for.  Unless there is an obvious date this should be, like for a historic reset, then this is the valuation date. | 
**dependency_type** | **str** | The available values are: Opaque, Cash, Discounting, EquityCurve, EquityVol, Fx, FxForwards, FxVol, IndexProjection, IrVol, Quote, Vendor | 

## Example

```python
from lusid.models.equity_curve_dependency_all_of import EquityCurveDependencyAllOf

# TODO update the JSON string below
json = "{}"
# create an instance of EquityCurveDependencyAllOf from a JSON string
equity_curve_dependency_all_of_instance = EquityCurveDependencyAllOf.from_json(json)
# print the JSON string representation of the object
print EquityCurveDependencyAllOf.to_json()

# convert the object into a dict
equity_curve_dependency_all_of_dict = equity_curve_dependency_all_of_instance.to_dict()
# create an instance of EquityCurveDependencyAllOf from a dict
equity_curve_dependency_all_of_form_dict = equity_curve_dependency_all_of.from_dict(equity_curve_dependency_all_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


