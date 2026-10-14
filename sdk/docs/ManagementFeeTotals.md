# ManagementFeeTotals

The management fee totals over every partner.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gross** | **float** | The fee before offsets. | 
**offset** | **float** | The offset applied to the fee. | 
**net** | **float** | The fee after offsets. | 
**carried_forward** | **float** | Offset in excess of the fee, carried forward to the next period. | 
## Example

```python
from lusid.models.management_fee_totals import ManagementFeeTotals
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

gross: Union[StrictFloat, StrictInt] = # Replace with your value
offset: Union[StrictFloat, StrictInt] = # Replace with your value
net: Union[StrictFloat, StrictInt] = # Replace with your value
carried_forward: Union[StrictFloat, StrictInt] = # Replace with your value
management_fee_totals_instance = ManagementFeeTotals(gross=gross, offset=offset, net=net, carried_forward=carried_forward)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

