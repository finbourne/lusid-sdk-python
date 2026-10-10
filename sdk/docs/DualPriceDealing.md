# DualPriceDealing

The bid and offer dealing prices a share class of a Dual fund publishes at a valuation point.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dealing_bid** | **float** | The price redemptions deal at, rounded as the share class unit price is. Absent when the class has no units in issue or the valuation did not price the side. | [optional] 
**dealing_offer** | **float** | The price subscriptions deal at, rounded as the share class unit price is. Absent when the class has no units in issue or the valuation did not price the side. | [optional] 
**bid_per_valuation_source** | **str** | The share class price the dealing bid was read or derived from: Bid when it is the bid read as published, Offer or Mid when it was derived from that price. Absent when nothing was dealt. | [optional] 
**offer_per_valuation_source** | **str** | The share class price the dealing offer was read or derived from: Offer when it is the offer read as published, Bid or Mid when it was derived from that price. Absent when nothing was dealt. | [optional] 
**bid_spread_bps** | **float** | The spread, in basis points, the dealing bid was set below the price it was derived from by. Absent when the bid was read. | [optional] 
**offer_spread_bps** | **float** | The spread, in basis points, the dealing offer was set above the price it was derived from by. Absent when the offer was read. | [optional] 
## Example

```python
from lusid.models.dual_price_dealing import DualPriceDealing
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

dealing_bid: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
dealing_offer: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
bid_per_valuation_source: Optional[StrictStr] = "example_bid_per_valuation_source"
offer_per_valuation_source: Optional[StrictStr] = "example_offer_per_valuation_source"
bid_spread_bps: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
offer_spread_bps: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
dual_price_dealing_instance = DualPriceDealing(dealing_bid=dealing_bid, dealing_offer=dealing_offer, bid_per_valuation_source=bid_per_valuation_source, offer_per_valuation_source=offer_per_valuation_source, bid_spread_bps=bid_spread_bps, offer_spread_bps=offer_spread_bps)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

