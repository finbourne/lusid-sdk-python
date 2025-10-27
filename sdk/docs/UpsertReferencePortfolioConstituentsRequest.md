# UpsertReferencePortfolioConstituentsRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**effective_from** | **str** | The first date from which the weights will apply | 
**weight_type** | **str** | The available values are: Static, Floating, Periodical | 
**period_type** | **str** | The available values are: Daily, Weekly, Monthly, Quarterly, Annually | [optional] 
**period_count** | **int** |  | [optional] 
**constituents** | [**List[ReferencePortfolioConstituentRequest]**](ReferencePortfolioConstituentRequest.md) | Set of constituents (instrument/weight pairings) | 
## Example

```python
from lusid.models.upsert_reference_portfolio_constituents_request import UpsertReferencePortfolioConstituentsRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

effective_from: StrictStr = "example_effective_from"
weight_type: StrictStr = "example_weight_type"
period_type: Optional[StrictStr] = "example_period_type"
period_count: Optional[StrictInt] = # Replace with your value
period_count: Optional[StrictInt] = None
constituents: List[ReferencePortfolioConstituentRequest] = # Replace with your value
upsert_reference_portfolio_constituents_request_instance = UpsertReferencePortfolioConstituentsRequest(effective_from=effective_from, weight_type=weight_type, period_type=period_type, period_count=period_count, constituents=constituents)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

