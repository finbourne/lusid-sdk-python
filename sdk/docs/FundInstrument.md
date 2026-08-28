# FundInstrument

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instrument_identifiers** | **Dict[str, Optional[str]]** | Unique instrument identifiers. Must only point to the same instrument | 
## Example

```python
from lusid.models.fund_instrument import FundInstrument
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

instrument_identifiers: Dict[str, Optional[StrictStr]] = # Replace with your value
fund_instrument_instance = FundInstrument(instrument_identifiers=instrument_identifiers)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

