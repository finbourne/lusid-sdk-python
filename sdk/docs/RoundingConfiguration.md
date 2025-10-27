# RoundingConfiguration

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stock_units** | [**RoundingConfigurationComponent**](RoundingConfigurationComponent.md) |  | [optional] 
## Example

```python
from lusid.models.rounding_configuration import RoundingConfiguration
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

stock_units: Optional[RoundingConfigurationComponent] = # Replace with your value
rounding_configuration_instance = RoundingConfiguration(stock_units=stock_units)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

