# SwingPricingRule

Moves a NAV type's pricing basis with its net dealing flow. When the flow, as a percentage of the previous  valuation point's NAV, exceeds the threshold the fund is valued on the inflow or outflow basis instead of  the NAV type's own basis.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**threshold_percentage_of_nav** | **float** | The net dealing flow, as a percentage of the previous valuation point&#39;s NAV, above which the fund swings. Must be zero or more; zero swings on any non-zero flow. | 
**inflow_basis** | **str** | The pricing basis the fund is valued on when net subscriptions exceed the threshold: Mid, Bid or Ask. Defaults to Ask. Available values: Mid, Bid, Ask. | [optional] 
**outflow_basis** | **str** | The pricing basis the fund is valued on when net redemptions exceed the threshold: Mid, Bid or Ask. Defaults to Bid. Available values: Mid, Bid, Ask. | [optional] 
## Example

```python
from lusid.models.swing_pricing_rule import SwingPricingRule
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

threshold_percentage_of_nav: Union[StrictFloat, StrictInt] = # Replace with your value
inflow_basis: Optional[StrictStr] = "example_inflow_basis"
outflow_basis: Optional[StrictStr] = "example_outflow_basis"
swing_pricing_rule_instance = SwingPricingRule(threshold_percentage_of_nav=threshold_percentage_of_nav, inflow_basis=inflow_basis, outflow_basis=outflow_basis)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

