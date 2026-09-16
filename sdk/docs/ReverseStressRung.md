# ReverseStressRung

One evaluated factor and what the portfolio was worth under it.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scale** | **float** | The factor the scenario&#39;s shifts were multiplied by. | [optional] 
**value** | **float** | The value of the measure under the scaled scenario. | [optional] 
**pnl** | **float** | The change from the unstressed value. | [optional] 
## Example

```python
from lusid.models.reverse_stress_rung import ReverseStressRung
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

scale: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
value: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
pnl: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
reverse_stress_rung_instance = ReverseStressRung(scale=scale, value=value, pnl=pnl)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

