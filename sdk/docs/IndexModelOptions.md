# IndexModelOptions

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**portfolio_scaling** | **str** | The available values are: Sum, AbsoluteSum, Unity | 
**model_options_type** | **str** | The available values are: Invalid, OpaqueModelOptions, EmptyModelOptions, IndexModelOptions, FxForwardModelOptions, FundingLegModelOptions, EquityModelOptions, CdsModelOptions | 
## Example

```python
from lusid.models.index_model_options import IndexModelOptions
from typing import Any, Dict
from pydantic.v1 import Field, StrictStr, validator

portfolio_scaling: StrictStr = "example_portfolio_scaling"
model_options_type: StrictStr = "example_model_options_type"
index_model_options_instance = IndexModelOptions(portfolio_scaling=portfolio_scaling, model_options_type=model_options_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

