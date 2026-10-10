# SwingSpreads

The stored spreads a Single fund swings by, one set for each direction of net cashflow.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inflow** | [**DirectionSpreads**](DirectionSpreads.md) |  | [optional] 
**outflow** | [**DirectionSpreads**](DirectionSpreads.md) |  | [optional] 
## Example

```python
from lusid.models.swing_spreads import SwingSpreads
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

inflow: Optional[DirectionSpreads] = None
outflow: Optional[DirectionSpreads] = None
swing_spreads_instance = SwingSpreads(inflow=inflow, outflow=outflow)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

