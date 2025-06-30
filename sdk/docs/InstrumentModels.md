# InstrumentModels

Supported pricing models for an instrument.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instrument_id** | **str** | The unique LUSID Instrument Identifier (LUID) of the instrument. | [optional] 
**supported_models** | **List[str]** | The pricing models supported by the instrument e.g. &#39;Discounting&#39;. | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.instrument_models import InstrumentModels
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, conlist

instrument_id: Optional[StrictStr] = "example_instrument_id"
supported_models: Optional[conlist(StrictStr)] = # Replace with your value
links: Optional[conlist(Link)] = None
instrument_models_instance = InstrumentModels(instrument_id=instrument_id, supported_models=supported_models, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

