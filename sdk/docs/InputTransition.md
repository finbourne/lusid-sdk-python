# InputTransition

The input 'transition' within a corporate action, representing the singular input position
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**units_factor** | **float** | The factor to scale units by | 
**cost_factor** | **float** | The factor to scale cost by | 
## Example

```python
from lusid.models.input_transition import InputTransition
from typing import Any, Dict, Union
from pydantic.v1 import BaseModel, Field, StrictFloat, StrictInt

units_factor: Union[StrictFloat, StrictInt] = # Replace with your value
cost_factor: Union[StrictFloat, StrictInt] = # Replace with your value
input_transition_instance = InputTransition(units_factor=units_factor, cost_factor=cost_factor)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

