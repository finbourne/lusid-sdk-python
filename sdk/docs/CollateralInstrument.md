# CollateralInstrument

Wrapper for one instrument in a larger collateral basket, as part of a repurchase agreement modelled as a FlexibleRepo.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**units** | **float** | The amount of the instrument in the basket for this repurchase agreement. | 
**instrument** | [**MasteredInstrument**](MasteredInstrument.md) |  | 
## Example

```python
from lusid.models.collateral_instrument import CollateralInstrument
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

units: Union[StrictFloat, StrictInt] = # Replace with your value
instrument: MasteredInstrument
collateral_instrument_instance = CollateralInstrument(units=units, instrument=instrument)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

