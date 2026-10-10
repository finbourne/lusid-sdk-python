# PricingMethodologyOverrideRequest

A fund manager's choice of basis for a valuation point's dealing price, in place of the pricing methodology's  decision. The spread still comes from the methodology.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**decision** | **str** | The basis the dealing price is published on: Mid, Bid or Offer. Under a Stored spread source the spread for Bid or Offer is the stored tier the net cashflow matches in that direction, or that direction&#39;s first tier when the flow is below every tier. Under a Market spread source Bid or Offer reads that side&#39;s price including notional dealing costs, which every active NAV type&#39;s valuation recipe must publish. Available values: Mid, Bid, Offer. | 
**reason** | **str** | Why the fund manager overrode the methodology&#39;s decision. | 
## Example

```python
from lusid.models.pricing_methodology_override_request import PricingMethodologyOverrideRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

decision: StrictStr = "example_decision"
reason: StrictStr = "example_reason"
pricing_methodology_override_request_instance = PricingMethodologyOverrideRequest(decision=decision, reason=reason)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

