# HoldingPricingInfo

Enables price quotes to be created from Holding fields as either overrides or fallbacks to the Market Data resolution process. For example, we may wish to price an instrument at Cost if Market Data resolution fails. We may also wish to always price Bonds using the LastTradedPrice on the corresponding Holding.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fallback_field** | **str** | The default Holding field to fall back on if the Market Data resolution process fails to find a price quote. | [optional] 
**override_field** | **str** | The default Holding field to be used as an override for instrument price quotes. This cannot be specified along with a FallbackField or any SpecificFallbacks, since we&#39;ll never attempt Market Data resolution for price quotes if this field is populated. | [optional] 
**specific_fallbacks** | [**List[SpecificHoldingPricingInfo]**](SpecificHoldingPricingInfo.md) | Allows a user to specify fallbacks using Holding fields for sources that match a particular DependencySourceFilter. | [optional] 
**specific_overrides** | [**List[SpecificHoldingPricingInfo]**](SpecificHoldingPricingInfo.md) | Allows a user to specify overrides using Holding fields for sources that match a particular DependencySourceFilter. | [optional] 
## Example

```python
from lusid.models.holding_pricing_info import HoldingPricingInfo
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, conlist

fallback_field: Optional[StrictStr] = "example_fallback_field"
override_field: Optional[StrictStr] = "example_override_field"
specific_fallbacks: Optional[conlist(SpecificHoldingPricingInfo)] = # Replace with your value
specific_overrides: Optional[conlist(SpecificHoldingPricingInfo)] = # Replace with your value
holding_pricing_info_instance = HoldingPricingInfo(fallback_field=fallback_field, override_field=override_field, specific_fallbacks=specific_fallbacks, specific_overrides=specific_overrides)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

