# CalculationInfo

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**calculation_method** | **str** | Method of calculating the fees or commission among: BasisPoints, Percentage, Rate, Flat etc. | 
**multiplier** | **str** | Field by which to multiply the numerical amount. Eg: Quantity, Value | 
**calculation_amount** | **float** | Numerical fee amount | 
## Example

```python
from lusid.models.calculation_info import CalculationInfo
from typing import Any, Dict, Union
from pydantic.v1 import BaseModel, Field, StrictFloat, StrictInt, constr

calculation_method: StrictStr = "example_calculation_method"
multiplier: StrictStr = "example_multiplier"
calculation_amount: Union[StrictFloat, StrictInt] = # Replace with your value
calculation_info_instance = CalculationInfo(calculation_method=calculation_method, multiplier=multiplier, calculation_amount=calculation_amount)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

