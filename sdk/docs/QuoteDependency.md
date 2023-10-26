# QuoteDependency

For indicating a dependency on the value of an asset at a point in time.  If the time is omitted, then the dependency is interpreted as the latest value with respect to anything observing it.  E.g. An EquitySwap will declare a dependency on the current price of the underlying equity.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**market_identifier** | **str** | Type of the code identifying the asset, e.g. ISIN or CUSIP | 
**code** | **str** | The code identifying the corresponding equity, e.g. US0378331005 if the MarketIdentifier was set to ISIN | 
**var_date** | **datetime** | The effectiveAt of the quote for the identified entity. | 
**dependency_type** | **str** | The available values are: OpaqueDependency, CashDependency, DiscountingDependency, EquityCurveDependency, EquityVolDependency, FxDependency, FxForwardsDependency, FxVolDependency, IndexProjectionDependency, IrVolDependency, QuoteDependency, Vendor, CalendarDependency, InflationFixingDependency | 

## Example

```python
from lusid.models.quote_dependency import QuoteDependency

# TODO update the JSON string below
json = "{}"
# create an instance of QuoteDependency from a JSON string
quote_dependency_instance = QuoteDependency.from_json(json)
# print the JSON string representation of the object
print QuoteDependency.to_json()

# convert the object into a dict
quote_dependency_dict = quote_dependency_instance.to_dict()
# create an instance of QuoteDependency from a dict
quote_dependency_form_dict = quote_dependency.from_dict(quote_dependency_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


