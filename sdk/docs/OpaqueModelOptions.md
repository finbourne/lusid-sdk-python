# OpaqueModelOptions

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **Dict[str, Optional[object]]** |  | 
**model_options_type** | **str** | The available values are: Invalid, OpaqueModelOptions, EmptyModelOptions, IndexModelOptions, FxForwardModelOptions, FundingLegModelOptions, EquityModelOptions, CdsModelOptions | 
## Example

```python
from lusid.models.opaque_model_options import OpaqueModelOptions
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

data: Dict[str, Any]
model_options_type: StrictStr = "example_model_options_type"
opaque_model_options_instance = OpaqueModelOptions(data=data, model_options_type=model_options_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

