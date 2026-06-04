# SecurityOfferConstituent

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new_instrument** | [**NewInstrument**](NewInstrument.md) |  | 
**units_ratio** | [**UnitsRatio**](UnitsRatio.md) |  | 
**settlement_date** | **datetime** |  | 
**min_piece_size** | **float** |  | [optional] 
**min_increment** | **float** |  | [optional] 
## Example

```python
from lusid.models.security_offer_constituent import SecurityOfferConstituent
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

new_instrument: NewInstrument = # Replace with your value
units_ratio: UnitsRatio = # Replace with your value
settlement_date: datetime = # Replace with your value
min_piece_size: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
min_increment: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
security_offer_constituent_instance = SecurityOfferConstituent(new_instrument=new_instrument, units_ratio=units_ratio, settlement_date=settlement_date, min_piece_size=min_piece_size, min_increment=min_increment)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

