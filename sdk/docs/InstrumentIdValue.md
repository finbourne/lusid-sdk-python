# InstrumentIdValue

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | The value of the identifier. | 
**effective_at** | **datetime** | The effective datetime from which the identifier will be valid. If left unspecified the default value is the beginning of time. | [optional] 
## Example

```python
from lusid.models.instrument_id_value import InstrumentIdValue
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

value: StrictStr = "example_value"
effective_at: Optional[datetime] = # Replace with your value
instrument_id_value_instance = InstrumentIdValue(value=value, effective_at=effective_at)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

