# SimpleRoundingConvention

Certain bonds will follow certain rounding conventions.  For example, Thai government bonds will round accrued interest and cashflow values 2dp, whereas for  French government bonds, the rounding is to 7dp.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**precision** | **int** | The precision of the rounding. The decimal places or significant figures to which the rounding takes place.  Defaults to 0 if not set. | [optional] 
**rounding_type** | **str** | The type of rounding.  e.g. Round Up, Round Down    Supported string (enumeration) values are: [Down, Up, Nearest].  Defaults to \&quot;None\&quot; if not set. | [optional] 
## Example

```python
from lusid.models.simple_rounding_convention import SimpleRoundingConvention
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, StrictInt, StrictStr

precision: Optional[StrictInt] = # Replace with your value
precision: Optional[StrictInt] = None
rounding_type: Optional[StrictStr] = "example_rounding_type"
simple_rounding_convention_instance = SimpleRoundingConvention(precision=precision, rounding_type=rounding_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

