# InstrumentActivityAdjustment

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nav_activity_adjustment_source** | **str** | The post closed activity source of the given entity, for example Manual. Available values: Undefined, Manual, Auto. | 
**as_at** | **datetime** | The asAt time for which the adjustment is being applied. | 
**scope** | **str** | The Scope of the given entity | 
**lusid_instrument_id** | **str** | The LusidInstrumentId of the given entity | 
**nav_activity_adjustment_type** | **str** | The type of the entity being applied, for example a PortfolioTransaction. Available values: PortfolioTransactionAdjustment, PortfolioSettlementInstructionAdjustment, InstrumentActivityAdjustment, QuoteActivityAdjustment. | 
## Example

```python
from lusid.models.instrument_activity_adjustment import InstrumentActivityAdjustment
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

nav_activity_adjustment_source: StrictStr = "example_nav_activity_adjustment_source"
as_at: datetime = # Replace with your value
scope: StrictStr = "example_scope"
lusid_instrument_id: StrictStr = "example_lusid_instrument_id"
nav_activity_adjustment_type: StrictStr = "example_nav_activity_adjustment_type"
instrument_activity_adjustment_instance = InstrumentActivityAdjustment(nav_activity_adjustment_source=nav_activity_adjustment_source, as_at=as_at, scope=scope, lusid_instrument_id=lusid_instrument_id, nav_activity_adjustment_type=nav_activity_adjustment_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

