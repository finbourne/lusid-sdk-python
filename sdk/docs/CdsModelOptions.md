# CdsModelOptions

Model options for credit default instrument.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**use_factors_for_current_notional** | **bool** | Determines if calculations that use current notional apply use a constituent weight factor from a quote representing a default. | 
**model_options_type** | **str** | The available values are: Invalid, OpaqueModelOptions, EmptyModelOptions, IndexModelOptions, FxForwardModelOptions, FundingLegModelOptions, EquityModelOptions, CdsModelOptions | 
## Example

```python
from lusid.models.cds_model_options import CdsModelOptions
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

use_factors_for_current_notional: StrictBool = # Replace with your value
use_factors_for_current_notional:StrictBool = True
model_options_type: StrictStr = "example_model_options_type"
cds_model_options_instance = CdsModelOptions(use_factors_for_current_notional=use_factors_for_current_notional, model_options_type=model_options_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

