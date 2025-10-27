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
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

instrument_id: Optional[StrictStr] = "example_instrument_id"
supported_models: Optional[List[StrictStr]] = # Replace with your value
links: Optional[List[Link]] = None
instrument_models_instance = InstrumentModels(instrument_id=instrument_id, supported_models=supported_models, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

