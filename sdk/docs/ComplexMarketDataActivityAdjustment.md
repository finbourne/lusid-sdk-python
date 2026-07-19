# ComplexMarketDataActivityAdjustment

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nav_activity_adjustment_source** | **str** | The post closed activity source of the given entity, for example Manual. Available values: Undefined, Manual, Auto. | 
**as_at** | **datetime** | The asAt time for which the adjustment is being applied. | 
**effective_at** | **str** | The EffectiveAt time of the entity event that need to be added to the closed period. | 
**entity_unique_id** | **str** | The EntityUniqueId from the entity which needs to be added as a post close activity. | 
**nav_activity_adjustment_type** | **str** | The type of the entity being applied, for example a PortfolioTransaction. Available values: PortfolioTransactionAdjustment, PortfolioSettlementInstructionAdjustment, InstrumentActivityAdjustment, QuoteActivityAdjustment, ComplexMarketDataActivityAdjustment. | 
## Example

```python
from lusid.models.complex_market_data_activity_adjustment import ComplexMarketDataActivityAdjustment
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

nav_activity_adjustment_source: StrictStr = "example_nav_activity_adjustment_source"
as_at: datetime = # Replace with your value
effective_at: StrictStr = "example_effective_at"
entity_unique_id: StrictStr = "example_entity_unique_id"
nav_activity_adjustment_type: StrictStr = "example_nav_activity_adjustment_type"
complex_market_data_activity_adjustment_instance = ComplexMarketDataActivityAdjustment(nav_activity_adjustment_source=nav_activity_adjustment_source, as_at=as_at, effective_at=effective_at, entity_unique_id=entity_unique_id, nav_activity_adjustment_type=nav_activity_adjustment_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

