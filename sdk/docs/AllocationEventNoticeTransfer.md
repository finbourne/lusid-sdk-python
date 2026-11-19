# AllocationEventNoticeTransfer

The transfer a notice reports, from the leg the partner is on: the other party to the leg, the lines the  interest moves between, the fraction and the terms.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**counterparty_investor_record_id** | **str** | The investor record on the other side of the leg: the transferor on the transferee&#39;s notice, the transferee on the transferor&#39;s. Absent when the register does not say who holds the source line. | [optional] 
**from_line_id** | **str** | The register line the interest moves from. | 
**to_line_id** | **str** | The register line the interest moves to. | 
**fraction** | **float** | The fraction of the source line transferred. | 
**pnl_split** | **str** | How the period&#39;s profit and loss is split around the transfer date: InterimClose or DailyProration. | 
**consideration** | [**AllocationEventTransferConsideration**](AllocationEventTransferConsideration.md) |  | [optional] 
**consent_reference** | **str** | A reference to the consent obtained for the transfer, when one was. | [optional] 
## Example

```python
from lusid.models.allocation_event_notice_transfer import AllocationEventNoticeTransfer
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

counterparty_investor_record_id: Optional[StrictStr] = "example_counterparty_investor_record_id"
from_line_id: StrictStr = "example_from_line_id"
to_line_id: StrictStr = "example_to_line_id"
fraction: Union[StrictFloat, StrictInt] = # Replace with your value
pnl_split: StrictStr = "example_pnl_split"
consideration: Optional[AllocationEventTransferConsideration] = None
consent_reference: Optional[StrictStr] = "example_consent_reference"
allocation_event_notice_transfer_instance = AllocationEventNoticeTransfer(counterparty_investor_record_id=counterparty_investor_record_id, from_line_id=from_line_id, to_line_id=to_line_id, fraction=fraction, pnl_split=pnl_split, consideration=consideration, consent_reference=consent_reference)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

