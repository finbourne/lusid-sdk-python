# PostCloseActivity

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_type** | **str** | The type of the entity, possible values are: * &#x60;PortfolioTransaction&#x60;, * &#x60;Instrument&#x60;, * &#x60;InstrumentEvent&#x60;, * &#x60;InstrumentEventInstruction&#x60;, * &#x60;PortfolioSettlementInstruction&#x60;, and, * &#x60;Quote&#x60;. | 
**entity_unique_id** | **str** | The entity unique ID. The expected format for each entity is: | entityType                       | entityUniqueId                                    | |----------------------------------|---------------------------------------------------| | &#x60;PortfolioTransaction&#x60;           | &#x60;portfolioUniqueId_transactionId&#x60;                 | | &#x60;Instrument&#x60;                     | &#x60;instrumentUniqueId&#x60;                              | | &#x60;InstrumentEvent&#x60;                | &#x60;corporateActionSourceUniqueId_instrumentEventId&#x60; | | &#x60;InstrumentEventInstruction&#x60;     | &#x60;portfolioUniqueId_instructionId&#x60;                 | | &#x60;PortfolioSettlementInstruction&#x60; | &#x60;portfolioUniqueId_settlementInstructionId&#x60;       | | &#x60;Quote&#x60;                          | &#x60;quoteSeriesUniqueId_quoteSeriesInstrumentId&#x60;     | | 
**as_at** | **datetime** | The &#x60;AsAt&#x60; time of the event that needs to be added to the closed period. | 
**effective_at** | **str** | The &#x60;EffectiveAt&#x60; time of the event that need to be added to the closed period. This can be a date or cut label. Only applicable for &#x60;Quote&#x60; post-close activities. | [optional] 
## Example

```python
from lusid.models.post_close_activity import PostCloseActivity
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

entity_type: StrictStr = "example_entity_type"
entity_unique_id: StrictStr = "example_entity_unique_id"
as_at: datetime = # Replace with your value
effective_at: Optional[StrictStr] = "example_effective_at"
post_close_activity_instance = PostCloseActivity(entity_type=entity_type, entity_unique_id=entity_unique_id, as_at=as_at, effective_at=effective_at)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

