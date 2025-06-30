# UnitsRatio

The number of units you have after the event (output) for a given number of units you have prior to the event (input).
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**input** | **float** | Input amount.  Denominator of the Ratio | 
**output** | **float** | Output amount. Numerator of the Ratio | 
## Example

```python
from lusid.models.units_ratio import UnitsRatio
from typing import Any, Dict, Union
from pydantic.v1 import BaseModel, Field, StrictFloat, StrictInt

input: Union[StrictFloat, StrictInt] = # Replace with your value
output: Union[StrictFloat, StrictInt] = # Replace with your value
units_ratio_instance = UnitsRatio(input=input, output=output)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

