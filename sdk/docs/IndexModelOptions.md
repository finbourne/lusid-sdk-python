# IndexModelOptions

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**portfolio_scaling** | **str** | The available values are: Sum, AbsoluteSum, Unity | 
**lookthrough_portfolio_relationship_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**model_options_type** | **str** | The available values are: Invalid, OpaqueModelOptions, EmptyModelOptions, IndexModelOptions, FxForwardModelOptions, FundingLegModelOptions, EquityModelOptions, CdsModelOptions | 
## Example

```python
from lusid.models.index_model_options import IndexModelOptions
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

portfolio_scaling: StrictStr = "example_portfolio_scaling"
lookthrough_portfolio_relationship_id: Optional[ResourceId] = # Replace with your value
model_options_type: StrictStr = "example_model_options_type"
index_model_options_instance = IndexModelOptions(portfolio_scaling=portfolio_scaling, lookthrough_portfolio_relationship_id=lookthrough_portfolio_relationship_id, model_options_type=model_options_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

