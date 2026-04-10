# WeightedAllocationServiceRunRequest

The request body for the RunAllocationServiceWithWeights endpoint.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**placement_ids** | [**List[ResourceId]**](ResourceId.md) | The set of Placement IDs to allocate. | 
**portfolio_weights** | [**List[PortfolioWeight]**](PortfolioWeight.md) | The set of Portfolios and their associated weights to use for allocation. | [optional] 
## Example

```python
from lusid.models.weighted_allocation_service_run_request import WeightedAllocationServiceRunRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

placement_ids: List[ResourceId] = # Replace with your value
portfolio_weights: Optional[List[PortfolioWeight]] = # Replace with your value
weighted_allocation_service_run_request_instance = WeightedAllocationServiceRunRequest(placement_ids=placement_ids, portfolio_weights=portfolio_weights)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

