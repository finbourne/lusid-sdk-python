# A2BCorrectionCause

A transaction behind a BackdatedCorrection movement, with the journal action that put it there
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_id** | **str** | The unique identifier of the transaction behind the correction. | [optional] 
**action** | **str** | How the late change reached the ledger: TrueUp for a transaction that was booked, Reversal for one that was cancelled, ReversalAndTrueUp for one that was amended. Available values: TrueUp, Reversal, ReversalAndTrueUp. | [optional] 
## Example

```python
from lusid.models.a2_b_correction_cause import A2BCorrectionCause
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

transaction_id: Optional[StrictStr] = "example_transaction_id"
action: Optional[StrictStr] = "example_action"
a2_b_correction_cause_instance = A2BCorrectionCause(transaction_id=transaction_id, action=action)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

