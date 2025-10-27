# FixedLegAllOfOverrides

Any overriding data for notionals, spreads or rates that would affect generation of a leg.  This supports the case where an amortisation schedule is given but otherwise generation is allowed as usual.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amortization** | **List[float]** |  | [optional] 
**spreads** | **List[float]** |  | [optional] 
## Example

```python
from lusid.models.fixed_leg_all_of_overrides import FixedLegAllOfOverrides
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

amortization: Optional[List[Union[StrictFloat, StrictInt]]] = # Replace with your value
spreads: Optional[List[Union[StrictFloat, StrictInt]]] = # Replace with your value
fixed_leg_all_of_overrides_instance = FixedLegAllOfOverrides(amortization=amortization, spreads=spreads)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

