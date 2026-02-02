# InstrumentActivity

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**as_at** | **datetime** | The asAt time for which the adjustment is being applied. | 
**scope** | **str** | The Scope of the given entity | 
**lusid_instrument_id** | **str** | The LusidInstrumentId of the given entity | 
**nav_activity_adjustment_type** | **str** | . The available values are: PortfolioTransaction, PortfolioSettlementInstruction, InstrumentActivity | 
## Example

```python
from lusid.models.instrument_activity import InstrumentActivity
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

as_at: datetime = # Replace with your value
scope: StrictStr = "example_scope"
lusid_instrument_id: StrictStr = "example_lusid_instrument_id"
nav_activity_adjustment_type: StrictStr = "example_nav_activity_adjustment_type"
instrument_activity_instance = InstrumentActivity(as_at=as_at, scope=scope, lusid_instrument_id=lusid_instrument_id, nav_activity_adjustment_type=nav_activity_adjustment_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

