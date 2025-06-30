# GeneratedEventDiagnostics

Represents a set of diagnostics per generatedEvent, where applicable.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instrument_event_id** | **str** |  | 
**type** | **str** |  | 
**detail** | **str** |  | 
**error_details** | **List[str]** |  | 
## Example

```python
from lusid.models.generated_event_diagnostics import GeneratedEventDiagnostics
from typing import Any, Dict, List
from pydantic.v1 import BaseModel, Field, StrictStr, conlist, constr

instrument_event_id: StrictStr = "example_instrument_event_id"
type: StrictStr = "example_type"
detail: StrictStr = "example_detail"
error_details: conlist(StrictStr) = # Replace with your value
generated_event_diagnostics_instance = GeneratedEventDiagnostics(instrument_event_id=instrument_event_id, type=type, detail=detail, error_details=error_details)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

