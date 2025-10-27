# WeightedInstruments

Class that models a set of instruments of which each has some quantity and can be identified by a unique label.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instruments** | [**List[WeightedInstrument]**](WeightedInstrument.md) | The instruments that are held in the set. | 
## Example

```python
from lusid.models.weighted_instruments import WeightedInstruments
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

instruments: List[WeightedInstrument] = # Replace with your value
weighted_instruments_instance = WeightedInstruments(instruments=instruments)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

