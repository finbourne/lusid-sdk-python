# AmortisationHorizon

The redemption a bond's cost is amortised towards, chosen per tax lot by whether the lot is held at a premium  (cost per unit above par) or a discount. Each value is one of Maturity, NextCall, NextPut or YieldToWorst and  defaults to Maturity. NextCall strikes a lot to its next call where the call price is below the lot's carrying  value, else to maturity until that call passes, so a discount lot is never struck to a call at or above par.  NextPut strikes to the next put at its price. YieldToWorst strikes to whichever call or the maturity gives the  lowest yield from the lot's cost.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**premium** | **str** | Available values: Maturity, NextCall, NextPut, YieldToWorst. | [optional] 
**discount** | **str** | Available values: Maturity, NextCall, NextPut, YieldToWorst. | [optional] 
## Example

```python
from lusid.models.amortisation_horizon import AmortisationHorizon
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

premium: Optional[StrictStr] = "example_premium"
discount: Optional[StrictStr] = "example_discount"
amortisation_horizon_instance = AmortisationHorizon(premium=premium, discount=discount)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

