# TranslateInstrumentDefinitionsRequest

A collection of instruments to translate, along with the target dialect to translate into.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instruments** | [**Dict[str, LusidInstrument]**](LusidInstrument.md) | The collection of instruments to translate.                Each instrument definition should be keyed by a unique correlation id. This id is ephemeral  and is not stored by LUSID. It serves only as a way to easily identify each instrument in the response.                Any instrument that is not already in the LUSID dialect should be given as an ExoticInstrument. | 
**dialect** | **str** | The target dialect that the given instruments should be translated to. | 
## Example

```python
from lusid.models.translate_instrument_definitions_request import TranslateInstrumentDefinitionsRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

instruments: Dict[str, LusidInstrument] = # Replace with your value
dialect: StrictStr = "example_dialect"
translate_instrument_definitions_request_instance = TranslateInstrumentDefinitionsRequest(instruments=instruments, dialect=dialect)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

