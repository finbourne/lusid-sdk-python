# FundingLegOptions

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expected_funding_leg_notional** | **str** | Assumption made on future expected notional of the funding leg. | 
**model_options_type** | **str** | The available values are: Invalid, OpaqueModelOptions, EmptyModelOptions, IndexModelOptions, FxForwardModelOptions, FundingLegModelOptions, EquityModelOptions, CdsModelOptions | 
## Example

```python
from lusid.models.funding_leg_options import FundingLegOptions
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

expected_funding_leg_notional: StrictStr = "example_expected_funding_leg_notional"
model_options_type: StrictStr = "example_model_options_type"
funding_leg_options_instance = FundingLegOptions(expected_funding_leg_notional=expected_funding_leg_notional, model_options_type=model_options_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

