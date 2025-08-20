# ModelOptions

Base class for representing model options in LUSID, which provide config for instrument analytics. This base class should not be directly instantiated; each supported ModelOptionsType has a corresponding inherited class.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model_options_type** | **str** | The available values are: Invalid, OpaqueModelOptions, EmptyModelOptions, IndexModelOptions, FxForwardModelOptions, FundingLegModelOptions, EquityModelOptions, CdsModelOptions | 
## Example

```python
from lusid.models.model_options import ModelOptions
from typing import Any, Dict, Union
from pydantic.v1 import BaseModel, Field, StrictStr, validator

model_options_type: StrictStr = "example_model_options_type"
model_options_instance = ModelOptions(model_options_type=model_options_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

