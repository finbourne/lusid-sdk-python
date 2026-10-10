# DualPriceDerivation

How a Dual fund derives its dealing prices from one real price by fixed spreads.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**real_side** | **str** | The price read from the valuation: Bid or Offer, from which the other side is derived, or Mid, the share class unit price, from which both sides are derived, for a fund whose market data has no bid or offer. Available values: Bid, Offer, Mid. | 
**include_ndc** | **bool** | Whether the real side is read including notional dealing costs, which needs the NAV type to have a notional dealing cost table. Must be false for Mid. | 
**bid_spread_bps** | **float** | How far below the real price the bid is set, in basis points of the real price. Zero or more. Required when the bid is derived, for an Offer or Mid real side, and absent for a Bid one. | [optional] 
**offer_spread_bps** | **float** | How far above the real price the offer is set, in basis points of the real price. Zero or more. Required when the offer is derived, for a Bid or Mid real side, and absent for an Offer one. | [optional] 
## Example

```python
from lusid.models.dual_price_derivation import DualPriceDerivation
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

real_side: StrictStr = "example_real_side"
include_ndc: StrictBool = # Replace with your value
include_ndc:StrictBool = True
bid_spread_bps: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
offer_spread_bps: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
dual_price_derivation_instance = DualPriceDerivation(real_side=real_side, include_ndc=include_ndc, bid_spread_bps=bid_spread_bps, offer_spread_bps=offer_spread_bps)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

