# AllocationEventTransfer

One leg of a Transfer Allocation Event: a fraction of a capital interest line moving to another line.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**from_line_id** | **str** | The identifier of the capital interest line the fraction moves from, as it appears on the register of one of the map&#39;s members. | 
**to_investor_record_id** | **str** | The investor record that receives the transferred interest. | 
**to_line_id** | **str** | The identifier of the capital interest line the fraction moves to. Created if it does not exist. | 
**to_portfolio_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**fraction** | **float** | The fraction of the source line transferred, greater than zero and at most one. One closes the source line. Each balance moved is the source balance times the fraction, truncated to the currency&#39;s minor unit, so any remainder stays with the transferor. | 
**pnl_split** | **str** | How the profit and loss of the period containing the transfer is split: InterimClose closes the books on the transfer date; DailyProration prorates by days held. Defaults to InterimClose. Available values: InterimClose, DailyProration. | [optional] 
**consideration** | [**AllocationEventTransferConsideration**](AllocationEventTransferConsideration.md) |  | [optional] 
**consent_reference** | **str** | A reference to the consent obtained for the transfer, when the fund requires one. | [optional] 
## Example

```python
from lusid.models.allocation_event_transfer import AllocationEventTransfer
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

from_line_id: StrictStr = "example_from_line_id"
to_investor_record_id: StrictStr = "example_to_investor_record_id"
to_line_id: StrictStr = "example_to_line_id"
to_portfolio_id: Optional[ResourceId] = # Replace with your value
fraction: Union[StrictFloat, StrictInt] = # Replace with your value
pnl_split: Optional[StrictStr] = "example_pnl_split"
consideration: Optional[AllocationEventTransferConsideration] = None
consent_reference: Optional[StrictStr] = "example_consent_reference"
allocation_event_transfer_instance = AllocationEventTransfer(from_line_id=from_line_id, to_investor_record_id=to_investor_record_id, to_line_id=to_line_id, to_portfolio_id=to_portfolio_id, fraction=fraction, pnl_split=pnl_split, consideration=consideration, consent_reference=consent_reference)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

