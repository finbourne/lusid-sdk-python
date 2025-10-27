# InstrumentMatch

A collection of instrument search results
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mastered_instruments** | [**List[InstrumentDefinition]**](InstrumentDefinition.md) | The collection of instruments found by the search which have been mastered within LUSID. | [optional] 
**external_instruments** | [**List[InstrumentDefinition]**](InstrumentDefinition.md) | The collection of instruments found by the search which have not been mastered within LUSID and instead found via OpenFIGI. | [optional] 
## Example

```python
from lusid.models.instrument_match import InstrumentMatch
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

mastered_instruments: Optional[List[InstrumentDefinition]] = # Replace with your value
external_instruments: Optional[List[InstrumentDefinition]] = # Replace with your value
instrument_match_instance = InstrumentMatch(mastered_instruments=mastered_instruments, external_instruments=external_instruments)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

