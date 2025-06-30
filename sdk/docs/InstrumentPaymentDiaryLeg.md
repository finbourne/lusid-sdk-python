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
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictInt, StrictStr, conlist

leg_index: Optional[StrictInt] = # Replace with your value
leg_index: Optional[StrictInt] = None
leg_id: Optional[StrictStr] = "example_leg_id"
rows: Optional[conlist(InstrumentPaymentDiaryRow)] = # Replace with your value
instrument_payment_diary_leg_instance = InstrumentPaymentDiaryLeg(leg_index=leg_index, leg_id=leg_id, rows=rows)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

