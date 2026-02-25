# QuoteActivity

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**as_at** | **datetime** | The asAt time for which the adjustment is being applied. | 
**effective_at** | **str** | The EffectiveAt time of the quote event that need to be added to the closed period. | 
**entity_unique_id** | **str** | The EntityUniqueId from the quote which needs to be added as a post close activity. | 
**instrument_id** | **str** | The InstrumentId from the quote which needs to be added as a post close activity. | 
**nav_activity_adjustment_type** | **str** | . The available values are: PortfolioTransaction, PortfolioSettlementInstruction, InstrumentActivity, QuoteActivity | 
## Example

```python
from lusid.models.quote_activity import QuoteActivity
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

as_at: datetime = # Replace with your value
effective_at: StrictStr = "example_effective_at"
entity_unique_id: StrictStr = "example_entity_unique_id"
instrument_id: StrictStr = "example_instrument_id"
nav_activity_adjustment_type: StrictStr = "example_nav_activity_adjustment_type"
quote_activity_instance = QuoteActivity(as_at=as_at, effective_at=effective_at, entity_unique_id=entity_unique_id, instrument_id=instrument_id, nav_activity_adjustment_type=nav_activity_adjustment_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

