# SideDefinition

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**side** | **str** | A unique label identifying the side definition. | 
**security** | **str** | The field or property key defining the side&#39;s security, or instrument. | 
**currency** | **str** | The field or property key defining the side&#39;s currency. | 
**rate** | **str** | The field or property key defining the side&#39;s rate. | 
**units** | **str** | The value, field or property key defining the side&#39;s units. | 
**amount** | **str** | The value, field or property key defining the side&#39;s amount | 
**notional_amount** | **str** | The value, field or property key defining the side&#39;s notional amount | [optional] 
**current_face** | **str** | The value, field or property key defining the side&#39;s current face / outstanding notional. | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.side_definition import SideDefinition
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

side: StrictStr = "example_side"
security: StrictStr = "example_security"
currency: StrictStr = "example_currency"
rate: StrictStr = "example_rate"
units: StrictStr = "example_units"
amount: StrictStr = "example_amount"
notional_amount: Optional[StrictStr] = "example_notional_amount"
current_face: Optional[StrictStr] = "example_current_face"
links: Optional[List[Link]] = None
side_definition_instance = SideDefinition(side=side, security=security, currency=currency, rate=rate, units=units, amount=amount, notional_amount=notional_amount, current_face=current_face, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

