# SwingPricingDecision

What the NAV type's swing pricing rule decided for a valuation point: the net dealing flow it measured, how  it compared with the threshold, and the pricing basis the point was valued on as a result.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**net_dealing_flow** | **float** | The net dealing flow the rule measured for the valuation point, in the fund currency. Subscriptions are positive and redemptions negative. | [optional] 
**net_dealing_flow_percentage_of_nav** | **float** | The net dealing flow as a percentage of the previous valuation point&#39;s NAV. Zero when there is no previous NAV to measure against. | [optional] 
**threshold_percentage_of_nav** | **float** | The threshold the rule compared the flow with. | [optional] 
**direction** | **str** | Whether the fund swung and which way: None, Inflow or Outflow. | [optional] 
**pricing_basis_applied** | **str** | The pricing basis the valuation point was valued on after the rule was applied. Absent when the fund did not swing and the NAV type defers to the recipe. | [optional] 
## Example

```python
from lusid.models.swing_pricing_decision import SwingPricingDecision
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

net_dealing_flow: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
net_dealing_flow_percentage_of_nav: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
threshold_percentage_of_nav: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
direction: Optional[StrictStr] = "example_direction"
pricing_basis_applied: Optional[StrictStr] = "example_pricing_basis_applied"
swing_pricing_decision_instance = SwingPricingDecision(net_dealing_flow=net_dealing_flow, net_dealing_flow_percentage_of_nav=net_dealing_flow_percentage_of_nav, threshold_percentage_of_nav=threshold_percentage_of_nav, direction=direction, pricing_basis_applied=pricing_basis_applied)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

