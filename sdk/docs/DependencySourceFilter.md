# DependencySourceFilter

Encapsulates parts of a market data rule relating not to the nature of the market data requested, but rather the nature of the thing (instrument/model) that is requesting it.  In the first instance, this includes the instrument type, asset class, and the currency of the underlying instrument.  This can be used to differentiate requests for market data according to the source of the request. See MarketDataSpecificRule.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instrument_type** | **str** | Specify that a rule should only apply if the market data is requested by an instrument of a given instrument type.  If null, then no filtering on instrument type is applied. | [optional] 
**asset_class** | **str** | Specify that a rule should only apply if the market data is requested by an instrument of a given asset class.  If null, then no filtering on asset class is applied. | [optional] 
**dom_ccy** | **str** | Specify that a rule should only apply if the market data is requested by an instrument with a given domestic currency.  If null, then no filtering on currency is applied. | [optional] 
**long_or_short_indicator** | **str** | Specify that a rule should apply if the market data is requested by a model with a given long or short indicator.  If none, then no filtering on LongOrShortIndicator is applied. | [optional] 
**address_key_filters** | [**List[AddressKeyFilter]**](AddressKeyFilter.md) | Specify that a rule should apply if the market data is requested by an instrument with features or properties  satisfying all the given address key filters. If an empty list is given, no additional filtering is done. | [optional] 
## Example

```python
from lusid.models.dependency_source_filter import DependencySourceFilter
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, conlist, constr

instrument_type: Optional[StrictStr] = "example_instrument_type"
asset_class: Optional[StrictStr] = "example_asset_class"
dom_ccy: Optional[StrictStr] = "example_dom_ccy"
long_or_short_indicator: Optional[StrictStr] = "example_long_or_short_indicator"
address_key_filters: Optional[conlist(AddressKeyFilter)] = # Replace with your value
dependency_source_filter_instance = DependencySourceFilter(instrument_type=instrument_type, asset_class=asset_class, dom_ccy=dom_ccy, long_or_short_indicator=long_or_short_indicator, address_key_filters=address_key_filters)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

