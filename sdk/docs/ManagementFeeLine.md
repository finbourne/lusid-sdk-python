# ManagementFeeLine

One partner's management fee for the period.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**investor_record_id** | **str** | The investor record the fee belongs to. | 
**basis_amount** | **float** | The capital the fee was charged on. | 
**rate** | **float** | The annual fee rate applied. | 
**day_count_fraction** | **float** | The fraction of a year the period covers, on an ACT/365 basis. | 
**gross** | **float** | The fee before offsets. | 
**offset** | **float** | The offset applied to the fee. | 
**net** | **float** | The fee after offsets. | 
**carried_forward** | **float** | Offset in excess of the fee, carried forward to the next period. | 
**waived** | **bool** | Whether the partner is fee-exempt and the fee was waived. | 
## Example

```python
from lusid.models.management_fee_line import ManagementFeeLine
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

investor_record_id: StrictStr = "example_investor_record_id"
basis_amount: Union[StrictFloat, StrictInt] = # Replace with your value
rate: Union[StrictFloat, StrictInt] = # Replace with your value
day_count_fraction: Union[StrictFloat, StrictInt] = # Replace with your value
gross: Union[StrictFloat, StrictInt] = # Replace with your value
offset: Union[StrictFloat, StrictInt] = # Replace with your value
net: Union[StrictFloat, StrictInt] = # Replace with your value
carried_forward: Union[StrictFloat, StrictInt] = # Replace with your value
waived: StrictBool = # Replace with your value
waived:StrictBool = True
management_fee_line_instance = ManagementFeeLine(investor_record_id=investor_record_id, basis_amount=basis_amount, rate=rate, day_count_fraction=day_count_fraction, gross=gross, offset=offset, net=net, carried_forward=carried_forward, waived=waived)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

