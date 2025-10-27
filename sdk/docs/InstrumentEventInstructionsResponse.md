# InstrumentEventInstructionsResponse

The collection of successfully upserted instructions, and the collection of failures for those instructions that could not be upserted
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | [**Dict[str, InstrumentEventInstruction]**](InstrumentEventInstruction.md) | The collection of successfully upserted instructions | [optional] 
**failed** | [**Dict[str, ErrorDetail]**](ErrorDetail.md) | The collection of error information for instructions that could not be upserted | [optional] 
## Example

```python
from lusid.models.instrument_event_instructions_response import InstrumentEventInstructionsResponse
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

values: Optional[Dict[str, InstrumentEventInstruction]] = # Replace with your value
failed: Optional[Dict[str, ErrorDetail]] = # Replace with your value
instrument_event_instructions_response_instance = InstrumentEventInstructionsResponse(values=values, failed=failed)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

