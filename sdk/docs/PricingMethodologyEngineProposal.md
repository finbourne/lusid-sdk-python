# PricingMethodologyEngineProposal

What the pricing methodology alone publishes for a share class, kept alongside any decision that replaces it.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**swung** | **bool** | Whether the methodology swings the price. | 
**swing_direction** | **str** | Offer or Bid when the methodology swings the price. Absent when it does not. | [optional] 
**spread_source** | **str** | Where the methodology&#39;s spread came from: Stored or Market. Absent when it does not swing. | [optional] 
**spread_bps** | **float** | The stored spread the methodology applies, in basis points. Absent when it does not swing or swings to a market price. | [optional] 
**dealing_price** | **float** | The dealing price the methodology publishes. Absent when the class has no units in issue. | [optional] 
## Example

```python
from lusid.models.pricing_methodology_engine_proposal import PricingMethodologyEngineProposal
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

swung: StrictBool = # Replace with your value
swung:StrictBool = True
swing_direction: Optional[StrictStr] = "example_swing_direction"
spread_source: Optional[StrictStr] = "example_spread_source"
spread_bps: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
dealing_price: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
pricing_methodology_engine_proposal_instance = PricingMethodologyEngineProposal(swung=swung, swing_direction=swing_direction, spread_source=spread_source, spread_bps=spread_bps, dealing_price=dealing_price)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

