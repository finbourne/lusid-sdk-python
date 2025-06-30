# RoundingConfiguration

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stock_units** | [**RoundingConfigurationComponent**](RoundingConfigurationComponent.md) |  | [optional] 
## Example

```python
from lusid.models.rounding_configuration import RoundingConfiguration
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field

stock_units: Optional[RoundingConfigurationComponent] = # Replace with your value
rounding_configuration_instance = RoundingConfiguration(stock_units=stock_units)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

