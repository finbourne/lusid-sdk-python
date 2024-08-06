# DependencySourceFilter

Encapsulates parts of a market data rule relating not to the nature of the market data requested, but rather the nature of the thing (instrument/model) that is requesting it.  In the first instance, this includes the instrument type, asset class, and the currency of the underlying instrument.  This can be used to differentiate requests for market data according to the source of the request. See MarketDataSpecificRule.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instrument_type** | **str** | Specify that a rule should only apply if the market data is requested by an instrument of a given instrument type.  If null, then no filtering on instrument type is applied. | [optional] 
**asset_class** | **str** | Specify that a rule should only apply if the market data is requested by an instrument of a given asset class.  If null, then no filtering on asset class is applied. | [optional] 
**dom_ccy** | **str** | Specify that a rule should only apply if the market data is requested by an instrument with a given domestic currency.  If null, then no filtering on currency is applied. | [optional] 
**long_or_short_indicator** | **str** | Specify that a rule should apply if the market data is requested by a model with a given long or short indicator.  If none, then no filtering on LongOrShortIndicator is applied. | [optional] 

## Example

```python
from lusid.models.dependency_source_filter import DependencySourceFilter

# TODO update the JSON string below
json = "{}"
# create an instance of DependencySourceFilter from a JSON string
dependency_source_filter_instance = DependencySourceFilter.from_json(json)
# print the JSON string representation of the object
print DependencySourceFilter.to_json()

# convert the object into a dict
dependency_source_filter_dict = dependency_source_filter_instance.to_dict()
# create an instance of DependencySourceFilter from a dict
dependency_source_filter_form_dict = dependency_source_filter.from_dict(dependency_source_filter_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


