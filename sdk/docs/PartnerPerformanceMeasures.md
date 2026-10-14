# PartnerPerformanceMeasures

One set of performance measures: the multiples, the net IRR and the cash flows it was solved from.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**commitment** | **float** | The total commitment the paid-in-capital ratio is measured against. | 
**paid_in** | **float** | The contributions paid in to the fund. | 
**distributed** | **float** | The distributions paid out of the fund. | 
**pic** | **float** | Paid-in capital as a multiple of commitment, or null when there is no commitment. | [optional] 
**dpi** | **float** | Distributions as a multiple of paid-in capital, or null when nothing has been paid in. | [optional] 
**rvpi** | **float** | Residual value as a multiple of paid-in capital, or null when nothing has been paid in. | [optional] 
**tvpi** | **float** | Total value as a multiple of paid-in capital, being DPI plus RVPI. | [optional] 
**net_irr** | **float** | The annualised net internal rate of return solved from the dated cash flows, or null when no rate can be solved. | [optional] 
**cash_flows** | [**List[PartnerPerformanceCashFlow]**](PartnerPerformanceCashFlow.md) | The dated cash flows the net IRR was solved from, including the terminal residual value. | 
**residual_value** | **float** | The partner&#39;s residual value in the fund at the valuation date. | 
**residual_value_date** | **datetime** | The date the residual value is taken as at. | 
## Example

```python
from lusid.models.partner_performance_measures import PartnerPerformanceMeasures
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

commitment: Union[StrictFloat, StrictInt] = # Replace with your value
paid_in: Union[StrictFloat, StrictInt] = # Replace with your value
distributed: Union[StrictFloat, StrictInt] = # Replace with your value
pic: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
dpi: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
rvpi: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
tvpi: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
net_irr: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
cash_flows: List[PartnerPerformanceCashFlow] = # Replace with your value
residual_value: Union[StrictFloat, StrictInt] = # Replace with your value
residual_value_date: datetime = # Replace with your value
partner_performance_measures_instance = PartnerPerformanceMeasures(commitment=commitment, paid_in=paid_in, distributed=distributed, pic=pic, dpi=dpi, rvpi=rvpi, tvpi=tvpi, net_irr=net_irr, cash_flows=cash_flows, residual_value=residual_value, residual_value_date=residual_value_date)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

