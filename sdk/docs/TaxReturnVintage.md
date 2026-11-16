# TaxReturnVintage

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**period_id** | **str** | The label of the period the amount falls into. | [optional] 
**start** | **datetime** | The first day of the period, inclusive. | [optional] 
**end** | **datetime** | The last day of the period, inclusive. | [optional] 
**deemed_gains** | **float** | The deemed gains arising at the end of the period. | [optional] 
**deemed_losses** | **float** | The deemed losses arising at the end of the period. | [optional] 
**net_amount** | **float** | The net deemed amount, gains less losses. | [optional] 
**carry_back_reduction** | **float** | The reduction to the net amount from losses carried back from later periods. | [optional] 
**spread_amount** | **float** | The net amount after carry-back that is spread over seven periods. | [optional] 
**outstanding** | **float** | The amount of the spread that has not yet been brought into charge. | [optional] 
## Example

```python
from lusid.models.tax_return_vintage import TaxReturnVintage
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

period_id: Optional[StrictStr] = "example_period_id"
start: Optional[datetime] = # Replace with your value
end: Optional[datetime] = # Replace with your value
deemed_gains: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
deemed_losses: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
net_amount: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
carry_back_reduction: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
spread_amount: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
outstanding: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
tax_return_vintage_instance = TaxReturnVintage(period_id=period_id, start=start, end=end, deemed_gains=deemed_gains, deemed_losses=deemed_losses, net_amount=net_amount, carry_back_reduction=carry_back_reduction, spread_amount=spread_amount, outstanding=outstanding)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

