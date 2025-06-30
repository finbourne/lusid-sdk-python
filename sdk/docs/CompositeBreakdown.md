# CompositeBreakdown

A list of Composite Breakdowns.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**effective_at** | **datetime** | The effectiveAt for the calculation. | 
**composite** | [**PortfolioReturnBreakdown**](PortfolioReturnBreakdown.md) |  | [optional] 
**constituents** | [**List[PortfolioReturnBreakdown]**](PortfolioReturnBreakdown.md) | The constituents with their information which are part of the composite. | [optional] 
## Example

```python
from lusid.models.composite_breakdown import CompositeBreakdown
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, conlist
from datetime import datetime
effective_at: datetime = # Replace with your value
composite: Optional[PortfolioReturnBreakdown] = None
constituents: Optional[conlist(PortfolioReturnBreakdown)] = # Replace with your value
composite_breakdown_instance = CompositeBreakdown(effective_at=effective_at, composite=composite, constituents=constituents)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

