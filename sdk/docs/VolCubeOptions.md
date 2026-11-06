# VolCubeOptions

Options for configuring how an IrVolCubeData is interpreted.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**day_count_convention** | **str** | Day count convention the vols are quoted on. The cube places its expiry pillars on it, and a swaption priced off  the cube measures its time to expiry on it. Supported values: Actual360, Actual365, Act365F, Act365_25 and  ActualActual, or their aliases Act360, MoneyMarket, Act365, ActAct and ActActIsda. Default value: ActualActual. Available values: Actual360, Act360, MoneyMarket, Actual365, Act365, Thirty360, ThirtyU360, Bond, ThirtyE360, EuroBond, ActualActual, ActAct, ActActIsda, ActActIcma, ActActIsma, OneOne, Act364, Act365F, Act365L, Act365_25, Act252, Bus252, NL360, NL365, ActActAFB, Act365Cad, ThirtyActIsda, Thirty365Isda, ThirtyEActIsda, ThirtyE360Isda, ThirtyE365Isda, ThirtyU360EOM, Invalid. | [optional] 
**market_data_options_type** | **str** | Available values: CurveOptions, VolCubeOptions. Available values: CurveOptions, VolCubeOptions. | 
## Example

```python
from lusid.models.vol_cube_options import VolCubeOptions
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

day_count_convention: Optional[StrictStr] = "example_day_count_convention"
market_data_options_type: StrictStr = "example_market_data_options_type"
vol_cube_options_instance = VolCubeOptions(day_count_convention=day_count_convention, market_data_options_type=market_data_options_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

