# FxTenorConvention

A wrapper of conventions that should be used when interpreting tenors in the context of FX. For instance, can be used to control how tenors are interpreted on an FxForwardTenorCurveData instance.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**calendar_code** | **str** | The code of the holiday calendar that should be used when interpreting FX tenors. | 
**spot_days** | **int** | The minimum number of business days that must pass within this calendar when calculating the spot date. | 
## Example

```python
from lusid.models.fx_tenor_convention import FxTenorConvention
from typing import Any, Dict
from pydantic.v1 import BaseModel, Field, StrictInt, constr

calendar_code: StrictStr = "example_calendar_code"
spot_days: StrictInt = # Replace with your value
spot_days: StrictInt = 42
fx_tenor_convention_instance = FxTenorConvention(calendar_code=calendar_code, spot_days=spot_days)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

