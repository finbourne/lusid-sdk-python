# EmptyModelOptions

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model_options_type** | **str** | The available values are: Invalid, OpaqueModelOptions, EmptyModelOptions, IndexModelOptions, FxForwardModelOptions, FundingLegModelOptions, EquityModelOptions, CdsModelOptions | 
## Example

```python
from lusid.models.empty_model_options import EmptyModelOptions
from typing import Any, Dict
from pydantic.v1 import Field, StrictStr, validator

model_options_type: StrictStr = "example_model_options_type"
empty_model_options_instance = EmptyModelOptions(model_options_type=model_options_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

