# RecordCounterpartyDemandRequest

The counterparty's figure for a margin call, to match against ours.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | The counterparty&#39;s figure for the call, signed as the call. | 
**received_at** | **datetime** | When the demand was received. Defaults to the current LUSID system datetime if not specified. | [optional] 
**statement_reference** | **str** | A reference to the counterparty&#39;s statement, such as a Drive path. Optional. | [optional] 
**note** | **str** | A note to record with the demand. Optional. | [optional] 
## Example

```python
from lusid.models.record_counterparty_demand_request import RecordCounterpartyDemandRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

amount: Union[StrictFloat, StrictInt] = # Replace with your value
received_at: Optional[datetime] = # Replace with your value
statement_reference: Optional[StrictStr] = "example_statement_reference"
note: Optional[StrictStr] = "example_note"
record_counterparty_demand_request_instance = RecordCounterpartyDemandRequest(amount=amount, received_at=received_at, statement_reference=statement_reference, note=note)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

