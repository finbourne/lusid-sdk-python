# LifeCycleEventLineage

The lineage of the event value
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_type** | **str** | The type of the event | [optional] 
**instrument_type** | **str** | The instrument type of the instrument for the event. | [optional] 
**instrument_id** | **str** | The LUID of the instrument for the event. | [optional] 
**leg_id** | **str** | Leg id for the event. | [optional] 
**source_transaction_id** | **str** | The source transaction of the instrument for the event. | [optional] 
## Example

```python
from lusid.models.life_cycle_event_lineage import LifeCycleEventLineage
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

event_type: Optional[StrictStr] = "example_event_type"
instrument_type: Optional[StrictStr] = "example_instrument_type"
instrument_id: Optional[StrictStr] = "example_instrument_id"
leg_id: Optional[StrictStr] = "example_leg_id"
source_transaction_id: Optional[StrictStr] = "example_source_transaction_id"
life_cycle_event_lineage_instance = LifeCycleEventLineage(event_type=event_type, instrument_type=instrument_type, instrument_id=instrument_id, leg_id=leg_id, source_transaction_id=source_transaction_id)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

