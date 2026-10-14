# SeriesBreakdown

The valuation of one series within a share class at a valuation point.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**series_identifier** | **str** | The identifier of the series within its share class. | 
**units** | **float** | The units in issue in the series at the valuation point. | 
**nav** | **float** | The series&#39; share of the share class NAV, in the fund currency. | 
**nav_per_unit** | **float** | The series NAV per unit in the share class currency, rounded as the share class unit price is. | 
**capital_ratio** | **float** | The series&#39; opening NAV as a proportion of the share class&#39;s opening NAV. Zero for a series with no units; sums to 1 across the series that hold units. | 
**pnl** | **float** | The P&amp;L apportioned to the series in the period: its NAV less its opening NAV. | 
**previous_nav** | **float** | The series NAV at the previous valuation point, in the fund currency. | 
## Example

```python
from lusid.models.series_breakdown import SeriesBreakdown
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

series_identifier: StrictStr = "example_series_identifier"
units: Union[StrictFloat, StrictInt] = # Replace with your value
nav: Union[StrictFloat, StrictInt] = # Replace with your value
nav_per_unit: Union[StrictFloat, StrictInt] = # Replace with your value
capital_ratio: Union[StrictFloat, StrictInt] = # Replace with your value
pnl: Union[StrictFloat, StrictInt] = # Replace with your value
previous_nav: Union[StrictFloat, StrictInt] = # Replace with your value
series_breakdown_instance = SeriesBreakdown(series_identifier=series_identifier, units=units, nav=nav, nav_per_unit=nav_per_unit, capital_ratio=capital_ratio, pnl=pnl, previous_nav=previous_nav)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

