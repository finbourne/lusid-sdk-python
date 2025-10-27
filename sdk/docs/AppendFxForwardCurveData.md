# AppendFxForwardCurveData

Used to append a new point to an FX curve defined using `FxForwardCurveData`.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **datetime** | Date for which the forward rate applies. | 
**rate** | **float** | Rate provided for the fx forward (price in FgnCcy per unit of DomCcy). | 
**market_data_type** | **str** | The available values are: AppendFxForwardCurveByQuoteReference, AppendFxForwardCurveData, AppendFxForwardPipsCurveData, AppendFxForwardTenorCurveData, AppendFxForwardTenorPipsCurveData | 
## Example

```python
from lusid.models.append_fx_forward_curve_data import AppendFxForwardCurveData
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

var_date: datetime = # Replace with your value
rate: Union[StrictFloat, StrictInt] = # Replace with your value
market_data_type: StrictStr = "example_market_data_type"
append_fx_forward_curve_data_instance = AppendFxForwardCurveData(var_date=var_date, rate=rate, market_data_type=market_data_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

