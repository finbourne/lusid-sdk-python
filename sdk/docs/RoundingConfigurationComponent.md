# RoundingConfigurationComponent

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rounding_type** | **str** | The type of rounding that should be used, eg: Up, Down, NearestRoundHalfAwayFromZero | 
## Example

```python
from lusid.models.rounding_configuration_component import RoundingConfigurationComponent
from typing import Any, Dict
from pydantic.v1 import BaseModel, Field, constr

rounding_type: StrictStr = "example_rounding_type"
rounding_configuration_component_instance = RoundingConfigurationComponent(rounding_type=rounding_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

