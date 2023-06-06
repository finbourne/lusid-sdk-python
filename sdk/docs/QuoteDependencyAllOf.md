# QuoteDependencyAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**market_identifier** | **str** | Type of the code identifying the asset, e.g. ISIN or CUSIP | 
**code** | **str** | The code identifying the corresponding equity, e.g. US0378331005 if the MarketIdentifier was set to ISIN | 
**var_date** | **datetime** | The effectiveAt of the quote for the identified entity. | 
**dependency_type** | **str** | The available values are: Opaque, Cash, Discounting, EquityCurve, EquityVol, Fx, FxForwards, FxVol, IndexProjection, IrVol, Quote, Vendor | 

## Example

```python
from lusid.models.quote_dependency_all_of import QuoteDependencyAllOf

# TODO update the JSON string below
json = "{}"
# create an instance of QuoteDependencyAllOf from a JSON string
quote_dependency_all_of_instance = QuoteDependencyAllOf.from_json(json)
# print the JSON string representation of the object
print QuoteDependencyAllOf.to_json()

# convert the object into a dict
quote_dependency_all_of_dict = quote_dependency_all_of_instance.to_dict()
# create an instance of QuoteDependencyAllOf from a dict
quote_dependency_all_of_form_dict = quote_dependency_all_of.from_dict(quote_dependency_all_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


