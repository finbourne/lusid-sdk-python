# ReturnZeroPvOptions

Options to indicate which errors to ignore when performing valuation.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instrument_matured** | **bool** | Indicates whether attempting to value an instrument after its maturity date should produce a failure (false)  or a zero PV (true). | [optional] 
## Example

```python
from lusid.models.return_zero_pv_options import ReturnZeroPvOptions
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

instrument_matured: Optional[StrictBool] = # Replace with your value
instrument_matured:Optional[StrictBool] = None
return_zero_pv_options_instance = ReturnZeroPvOptions(instrument_matured=instrument_matured)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

