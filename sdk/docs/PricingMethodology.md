# PricingMethodology

How a fund prices its share classes for dealing. A Single fund deals at one price per class, which starts at a  baseline and may swing with the fund's net cashflow. A Dual fund deals at a bid and an offer per class.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**output_shape** | **str** | How many dealing prices each share class publishes: Single, one price that subscriptions and redemptions both deal at, or Dual, a bid that redemptions deal at and an offer that subscriptions deal at. Available values: Single, Dual. | 
**swing_policy** | [**SwingPolicy**](SwingPolicy.md) |  | [optional] 
**price_labels** | **str** | What a Dual fund&#39;s two prices are. BidOffer is the only label available: the bid and the offer, including notional dealing costs, that the valuation recipe of each active NAV type publishes. Required for a Dual fund and must be omitted for a Single fund. Available values: BidOffer, CreationCancellation. | [optional] 
**derivation** | [**DualPriceDerivation**](DualPriceDerivation.md) |  | [optional] 
## Example

```python
from lusid.models.pricing_methodology import PricingMethodology
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

output_shape: StrictStr = "example_output_shape"
swing_policy: Optional[SwingPolicy] = # Replace with your value
price_labels: Optional[StrictStr] = "example_price_labels"
derivation: Optional[DualPriceDerivation] = None
pricing_methodology_instance = PricingMethodology(output_shape=output_shape, swing_policy=swing_policy, price_labels=price_labels, derivation=derivation)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

