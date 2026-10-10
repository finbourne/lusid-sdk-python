# SinglePriceDealing

The single dealing price a share class publishes at a valuation point.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dealing_price** | **float** | The price subscriptions and redemptions deal at, rounded as the share class unit price is. Absent when the class has no units in issue. | [optional] 
**swung** | **bool** | Whether the dealing price moved away from its baseline. | 
**swing_direction** | **str** | Offer when a net inflow swung the price up, Bid when a net outflow swung it down. Absent when the price did not swing. | [optional] 
**swing_from** | **str** | The baseline the price swung away from. Absent when it did not swing. | [optional] 
**per_valuation_source** | **str** | Bid or Offer when the dealing price is that side&#39;s share class price read as published, from a Bid or Offer baseline or a Market swing. Absent when the price is the mid or a stored spread was applied to it. | [optional] 
**spread_bps** | **float** | The stored spread applied, in basis points. Absent when the price did not swing or swung to a market price. | [optional] 
## Example

```python
from lusid.models.single_price_dealing import SinglePriceDealing
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

dealing_price: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
swung: StrictBool = # Replace with your value
swung:StrictBool = True
swing_direction: Optional[StrictStr] = "example_swing_direction"
swing_from: Optional[StrictStr] = "example_swing_from"
per_valuation_source: Optional[StrictStr] = "example_per_valuation_source"
spread_bps: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
single_price_dealing_instance = SinglePriceDealing(dealing_price=dealing_price, swung=swung, swing_direction=swing_direction, swing_from=swing_from, per_valuation_source=per_valuation_source, spread_bps=spread_bps)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

