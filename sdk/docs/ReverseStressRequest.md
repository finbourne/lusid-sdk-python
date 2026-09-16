# ReverseStressRequest

Request to solve a reverse stress test: instead of asking what a given market move does to a  portfolio, it asks how far the market has to move along a given direction to produce a given  loss. The direction is a stored scenario; the answer is the factor its shifts are multiplied by.                A single effective date is solved, not a schedule. \"How far must the market move to lose this  much\" has one answer per date, and returning a factor per date under one target would invite the  answer being read as a single portfolio-wide number when it is not.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recipe_id** | [**ResourceId**](ResourceId.md) |  | 
**portfolio_entity_ids** | [**List[PortfolioEntityId]**](PortfolioEntityId.md) | The portfolios or portfolio groups whose value the target loss is measured against. | 
**effective_at** | **datetime** | The effective date to value at. | 
**as_at** | **datetime** | The as-at time to read portfolios, instruments, market data and the scenario definition at.  Defaults to the latest. | [optional] 
**scenario** | [**ScenarioReference**](ScenarioReference.md) |  | 
**target_pnl** | **float** | The change in value to solve for, signed and in the report currency: negative for a loss.  Expressed as an amount rather than a percentage so that the same target can be stated against  a portfolio whose base value is not known to the caller. | 
**metric** | **str** | The measure the target is expressed in. Defaults to Valuation/PV. Must be a measure that  supports scenario decoration, which the request is rejected for if it is not. | [optional] 
**report_currency** | **str** | Three letter ISO currency string to report in. If absent the portfolio&#39;s own currency is used,  which makes the target ambiguous across a multi-currency portfolio group - supply it there. | [optional] 
**filters** | [**List[PropertyFilter]**](PropertyFilter.md) | Filters reducing the holdings the target is measured over, matching the valuation endpoint&#39;s. | [optional] 
**max_scale** | **float** | The largest factor to evaluate. A target beyond the loss reached at this factor is reported as  out of reach rather than extrapolated to: extrapolating past the evaluated range is exactly  where a locally linear P&amp;L stops being linear. | [optional] 
**ladder_points** | **int** | How many factors to evaluate between zero and MaxScale. All of them are valued in  one request - the rungs share market data resolution - so a finer ladder costs far less than  its rung count suggests, and a coarse one is the main source of a missed bracket. | [optional] 
**tolerance** | **float** | How close the achieved loss must be to the target, relative to the target&#39;s own size. Relative  rather than absolute because the same reverse stress is asked of books whose value differs by  orders of magnitude. | [optional] 
**max_iterations** | **int** | How many refinement rounds are allowed after the opening ladder. Each round costs one  valuation; on a near-linear P&amp;L the first interpolation is usually already inside tolerance,  so the default exists for the mildly curved case rather than the normal one. | [optional] 
## Example

```python
from lusid.models.reverse_stress_request import ReverseStressRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

recipe_id: ResourceId = # Replace with your value
portfolio_entity_ids: List[PortfolioEntityId] = # Replace with your value
effective_at: datetime = # Replace with your value
as_at: Optional[datetime] = # Replace with your value
scenario: ScenarioReference
target_pnl: Union[StrictFloat, StrictInt] = # Replace with your value
metric: Optional[StrictStr] = "example_metric"
report_currency: Optional[StrictStr] = "example_report_currency"
filters: Optional[List[PropertyFilter]] = # Replace with your value
max_scale: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
ladder_points: Optional[StrictInt] = # Replace with your value
ladder_points: Optional[StrictInt] = None
tolerance: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
max_iterations: Optional[StrictInt] = # Replace with your value
max_iterations: Optional[StrictInt] = None
reverse_stress_request_instance = ReverseStressRequest(recipe_id=recipe_id, portfolio_entity_ids=portfolio_entity_ids, effective_at=effective_at, as_at=as_at, scenario=scenario, target_pnl=target_pnl, metric=metric, report_currency=report_currency, filters=filters, max_scale=max_scale, ladder_points=ladder_points, tolerance=tolerance, max_iterations=max_iterations)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

