# EstimateValuationOutcome

Where a net cashflow leads the methodology: whether and which way it swings, the spread and tier it lands in, and the dealing price that results.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**swung** | **bool** | Whether the methodology swings the price on this net cashflow. | 
**swing_direction** | **str** | &#39;Bid&#39; or &#39;Offer&#39;, the side the price swings to. Absent when it does not swing. | [optional] 
**spread_bps** | **float** | The stored spread applied, in basis points. Absent when the price does not swing or the spread comes from the market. | [optional] 
**tier_matched** | [**SwingSpreadTierBounds**](SwingSpreadTierBounds.md) |  | [optional] 
**dealing_price** | **float** | The dealing price the methodology publishes on this net cashflow. Absent when the baseline price is unavailable. | [optional] 
## Example

```python
from lusid.models.estimate_valuation_outcome import EstimateValuationOutcome
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

swung: StrictBool = # Replace with your value
swung:StrictBool = True
swing_direction: Optional[StrictStr] = "example_swing_direction"
spread_bps: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
tier_matched: Optional[SwingSpreadTierBounds] = # Replace with your value
dealing_price: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
estimate_valuation_outcome_instance = EstimateValuationOutcome(swung=swung, swing_direction=swing_direction, spread_bps=spread_bps, tier_matched=tier_matched, dealing_price=dealing_price)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

