# InstrumentPaymentDiaryLeg

A leg containing a set of cashflows.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**leg_index** | **int** | Index (integer) for the leg of a payment diary. | [optional] 
**leg_id** | **str** | Identifier string for the leg of a payment diary. | [optional] 
**rows** | [**List[InstrumentPaymentDiaryRow]**](InstrumentPaymentDiaryRow.md) | List of individual cashflows within the payment diary. | [optional] 
## Example

```python
from lusid.models.instrument_payment_diary_leg import InstrumentPaymentDiaryLeg
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

leg_index: Optional[StrictInt] = # Replace with your value
leg_index: Optional[StrictInt] = None
leg_id: Optional[StrictStr] = "example_leg_id"
rows: Optional[List[InstrumentPaymentDiaryRow]] = # Replace with your value
instrument_payment_diary_leg_instance = InstrumentPaymentDiaryLeg(leg_index=leg_index, leg_id=leg_id, rows=rows)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

