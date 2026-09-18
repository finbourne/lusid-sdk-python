# CurrencyGroupMinorUnit

A minor unit currency within a currency group.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency** | **str** | The three to five letter, case-sensitive currency code of the minor unit, e.g. GBX. | 
**fraction_of_major** | **float** | The fraction of the major unit that one minor unit is worth, greater than zero and no more than one, e.g. 0.01 for GBX against GBP. | 
## Example

```python
from lusid.models.currency_group_minor_unit import CurrencyGroupMinorUnit
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

currency: StrictStr = "example_currency"
fraction_of_major: Union[Annotated[float, Field(strict=True)], Annotated[int, Field(strict=True)]] = Field(description="The fraction of the major unit that one minor unit is worth, greater than zero and no more than one, e.g. 0.01 for GBX against GBP.", alias="fractionOfMajor")
currency_group_minor_unit_instance = CurrencyGroupMinorUnit(currency=currency, fraction_of_major=fraction_of_major)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

