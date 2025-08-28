# TransactionSettlementBucket

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**settlement_category** | **str** | A category representing the set of movement types that this instruction applies to. | 
**lusid_instrument_id** | **str** | The LusidInstrumentId of the instrument being settled. | 
**instrument_scope** | **str** | The Scope of the instrument being settled. | 
**contractual_settlement_date** | **datetime** | The contractual settlement date. Used to match the instruction to the correct settlement bucket. | [optional] 
**contracted_units** | **float** | The contracted units. | [optional] 
**settled_units** | **float** | The settled units. | [optional] 
**unsettled_units** | **float** | The unsettled units. | [optional] 
**overdue_units** | **float** | The overdue units. | [optional] 
**configured_settlement** | **str** | The method of settlement for the settlement bucket, as defined in the portfolio&#39;s SettlementConfiguration | [optional] 
**status** | **str** | The Status of the settlement bucket - &#39;Settled&#39;, &#39;Part Settled&#39; or &#39;Unsettled&#39;. | 
**settlement_instructions** | [**List[TransactionSettlementInstruction]**](TransactionSettlementInstruction.md) | The settlement instructions received for this settlement bucket. | [optional] 
**movements** | [**List[TransactionSettlementMovement]**](TransactionSettlementMovement.md) | The movements for the settlement bucket. | [optional] 
## Example

```python
from lusid.models.transaction_settlement_bucket import TransactionSettlementBucket
from typing import Any, Dict, List, Optional, Union
from pydantic.v1 import BaseModel, Field, StrictFloat, StrictInt, StrictStr, conlist, constr
from datetime import datetime
settlement_category: StrictStr = "example_settlement_category"
lusid_instrument_id: StrictStr = "example_lusid_instrument_id"
instrument_scope: StrictStr = "example_instrument_scope"
contractual_settlement_date: Optional[datetime] = # Replace with your value
contracted_units: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
settled_units: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
unsettled_units: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
overdue_units: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
configured_settlement: Optional[StrictStr] = "example_configured_settlement"
status: StrictStr = "example_status"
settlement_instructions: Optional[conlist(TransactionSettlementInstruction)] = # Replace with your value
movements: Optional[conlist(TransactionSettlementMovement)] = # Replace with your value
transaction_settlement_bucket_instance = TransactionSettlementBucket(settlement_category=settlement_category, lusid_instrument_id=lusid_instrument_id, instrument_scope=instrument_scope, contractual_settlement_date=contractual_settlement_date, contracted_units=contracted_units, settled_units=settled_units, unsettled_units=unsettled_units, overdue_units=overdue_units, configured_settlement=configured_settlement, status=status, settlement_instructions=settlement_instructions, movements=movements)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

