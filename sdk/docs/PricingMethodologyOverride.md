# PricingMethodologyOverride

The fund manager's override a share class's dealing price follows instead of the pricing methodology's proposal,  and who made it when.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**decision** | **str** | The basis the dealing price is published on: Mid, Bid or Offer. Under a Stored spread source the spread for Bid or Offer is the stored tier the net cashflow matches in that direction, or that direction&#39;s first tier when the flow is below every tier. Under a Market spread source Bid or Offer reads that side&#39;s price including notional dealing costs, which every active NAV type&#39;s valuation recipe must publish. | 
**reason** | **str** | Why the fund manager overrode the methodology&#39;s decision. | 
**user** | **str** | The user who made the override. | [optional] 
**timestamp** | **datetime** | When the override was made. | 
**net_cashflow** | **float** | The fund&#39;s net dealing cashflow the decision was taken on, in the fund currency, read as at the override&#39;s timestamp. An inflow is positive and an outflow negative. A net that moves within its swing tier leaves the decision standing, so this can differ from the audit&#39;s current netCashflow, and both are kept on the final valuation point. Null when the swing policy approves automatically, or the decision was taken before the net was recorded. | [optional] 
## Example

```python
from lusid.models.pricing_methodology_override import PricingMethodologyOverride
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

decision: StrictStr = "example_decision"
reason: StrictStr = "example_reason"
user: Optional[StrictStr] = "example_user"
timestamp: datetime = # Replace with your value
net_cashflow: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
pricing_methodology_override_instance = PricingMethodologyOverride(decision=decision, reason=reason, user=user, timestamp=timestamp, net_cashflow=net_cashflow)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

