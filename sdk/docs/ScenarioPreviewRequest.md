# ScenarioPreviewRequest

Request to preview a scenario against a portfolio's market data without running a valuation: the  portfolio's market data dependencies are resolved and the scenario's shifts applied, and the  response reports which targets each shift changed (with values before and after) and which market  data was skipped. Supply either a reference to a stored scenario or inline shift definitions  (for previewing a definition before saving it), not both.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recipe_id** | [**ResourceId**](ResourceId.md) |  | 
**portfolio_entity_ids** | [**List[PortfolioEntityId]**](PortfolioEntityId.md) | The portfolios whose market data dependencies the scenario is previewed against. | 
**effective_at** | **datetime** | The effective date to resolve market data at. | 
**as_at** | **datetime** | The as-at time to resolve at. Defaults to the latest. | [optional] 
**scenario** | [**ScenarioReference**](ScenarioReference.md) |  | [optional] 
**shifts** | [**List[ScenarioShiftDefinition]**](ScenarioShiftDefinition.md) | Inline shift definitions to preview without saving a scenario, e.g. to test what a definition  would match while authoring it. Mutually exclusive with supplying a stored scenario reference. | [optional] 
## Example

```python
from lusid.models.scenario_preview_request import ScenarioPreviewRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

recipe_id: ResourceId = # Replace with your value
portfolio_entity_ids: List[PortfolioEntityId] = # Replace with your value
effective_at: datetime = # Replace with your value
as_at: Optional[datetime] = # Replace with your value
scenario: Optional[ScenarioReference] = None
shifts: Optional[List[ScenarioShiftDefinition]] = # Replace with your value
scenario_preview_request_instance = ScenarioPreviewRequest(recipe_id=recipe_id, portfolio_entity_ids=portfolio_entity_ids, effective_at=effective_at, as_at=as_at, scenario=scenario, shifts=shifts)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

