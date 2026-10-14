# CarryTierAmount

A partner's carry split by waterfall tier.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tier** | **str** | The waterfall tier. | 
**realised** | **float** | The carry realised in the tier. | 
**hypothetical** | **float** | The carry the tier would pay if the fund liquidated at the period end. | 
## Example

```python
from lusid.models.carry_tier_amount import CarryTierAmount
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

tier: StrictStr = "example_tier"
realised: Union[StrictFloat, StrictInt] = # Replace with your value
hypothetical: Union[StrictFloat, StrictInt] = # Replace with your value
carry_tier_amount_instance = CarryTierAmount(tier=tier, realised=realised, hypothetical=hypothetical)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

