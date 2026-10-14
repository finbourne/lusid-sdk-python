# AllocationEventNoticeLine

One line of a notice: an amount allocated to the partner under an ILPA transaction type.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ilpa_transaction_type** | **str** | The ILPA transaction type of the line. | 
**component** | **str** | The allocation event component the line is for. | [optional] 
**inside_fund** | **bool** | Whether the line moves capital inside the fund, as opposed to a fee or expense outside it. | 
**amount** | **float** | The amount of the line. | 
**unfunded_impact** | **float** | The effect of the line on the partner&#39;s unfunded commitment. | 
**recallable_until** | **datetime** | The date until which a recallable distribution may be recalled, or null. | [optional] 
## Example

```python
from lusid.models.allocation_event_notice_line import AllocationEventNoticeLine
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

ilpa_transaction_type: StrictStr = "example_ilpa_transaction_type"
component: Optional[StrictStr] = "example_component"
inside_fund: StrictBool = # Replace with your value
inside_fund:StrictBool = True
amount: Union[StrictFloat, StrictInt] = # Replace with your value
unfunded_impact: Union[StrictFloat, StrictInt] = # Replace with your value
recallable_until: Optional[datetime] = # Replace with your value
allocation_event_notice_line_instance = AllocationEventNoticeLine(ilpa_transaction_type=ilpa_transaction_type, component=component, inside_fund=inside_fund, amount=amount, unfunded_impact=unfunded_impact, recallable_until=recallable_until)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

