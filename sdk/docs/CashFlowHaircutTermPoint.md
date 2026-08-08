# CashFlowHaircutTermPoint

A point on a cashflow haircut term structure: the haircut rate applying at a given tenor from  the valuation date. Rates are linearly interpolated on time-to-payment between points and  extrapolated flat beyond either end of the term structure.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenor** | **str** | The tenor from the valuation date at which the rate applies, e.g. &#39;6M&#39; or &#39;5Y&#39;. | 
**rate** | **float** | The haircut rate applying at the tenor, as a fraction in the range [0, 1]. | 
## Example

```python
from lusid.models.cash_flow_haircut_term_point import CashFlowHaircutTermPoint
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

tenor: StrictStr = "example_tenor"
rate: Union[StrictFloat, StrictInt] = # Replace with your value
cash_flow_haircut_term_point_instance = CashFlowHaircutTermPoint(tenor=tenor, rate=rate)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

