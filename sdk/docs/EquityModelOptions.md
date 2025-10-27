# EquityModelOptions

Model options for equity related pricing.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**equity_forward_projection_type** | **str** | Determines how forward equity prices should be projected.                Supported string (enumeration) values are: [FlatForwardCurveFromSpot, EquityCurveByPrices, ForwardProjectedFromRatesCurve]. | 
**model_options_type** | **str** | The available values are: Invalid, OpaqueModelOptions, EmptyModelOptions, IndexModelOptions, FxForwardModelOptions, FundingLegModelOptions, EquityModelOptions, CdsModelOptions | 
## Example

```python
from lusid.models.equity_model_options import EquityModelOptions
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

equity_forward_projection_type: StrictStr = "example_equity_forward_projection_type"
model_options_type: StrictStr = "example_model_options_type"
equity_model_options_instance = EquityModelOptions(equity_forward_projection_type=equity_forward_projection_type, model_options_type=model_options_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

