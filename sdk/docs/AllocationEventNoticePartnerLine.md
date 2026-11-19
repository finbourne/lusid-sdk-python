# AllocationEventNoticePartnerLine

One register line a notice's partner was allocated on: the line, the fund whose register holds it, the line's  commitment at the event date and the partner's share landing on it.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**commitment_line_id** | **str** | The identifier of the register line. | 
**fund_id** | [**ResourceId**](ResourceId.md) |  | 
**commitment** | **float** | The line&#39;s committed capital at the event date. | 
**amount** | **float** | The partner&#39;s share of the event landing on the line, signed as the net amount due is. On a transfer, the committed capital moving on the line. | 
## Example

```python
from lusid.models.allocation_event_notice_partner_line import AllocationEventNoticePartnerLine
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

commitment_line_id: StrictStr = "example_commitment_line_id"
fund_id: ResourceId = # Replace with your value
commitment: Union[StrictFloat, StrictInt] = # Replace with your value
amount: Union[StrictFloat, StrictInt] = # Replace with your value
allocation_event_notice_partner_line_instance = AllocationEventNoticePartnerLine(commitment_line_id=commitment_line_id, fund_id=fund_id, commitment=commitment, amount=amount)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

