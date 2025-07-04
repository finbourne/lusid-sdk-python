# CompositeDispersion

A list of Dispersion calculations for the given years.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**effective_at** | **datetime** | The date for which dipsersion calculation has been done. This should be 31 Dec for each given year. | 
**dispersion_calculation** | **float** | The result for the dispersion calculation on the given effectiveAt. | [optional] 
**variance** | **float** | The variance on the given effectiveAt. | [optional] 
**first_quartile** | **float** | First Quartile (Q1) &#x3D;  (lower quartile) &#x3D; the middle of the bottom half of the returns. | [optional] 
**third_quartile** | **float** | Third Quartile (Q3) &#x3D;  (higher quartile) &#x3D; the middle of the top half of the returns. | [optional] 
**range** | **float** | Highest return - Lowest return. | [optional] 
**constituents_in_scope** | [**List[ResourceId]**](ResourceId.md) | List containing Composite members which are part of the dispersion calcualtion. | [optional] 
**constituents_excluded** | [**List[ResourceId]**](ResourceId.md) | List containing the Composite members which are not part of the dispersion calculation | [optional] 
## Example

```python
from lusid.models.composite_dispersion import CompositeDispersion
from typing import Any, Dict, List, Optional, Union
from pydantic.v1 import BaseModel, Field, StrictFloat, StrictInt, conlist
from datetime import datetime
effective_at: datetime = # Replace with your value
dispersion_calculation: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
variance: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
first_quartile: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
third_quartile: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
range: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
constituents_in_scope: Optional[conlist(ResourceId)] = # Replace with your value
constituents_excluded: Optional[conlist(ResourceId)] = # Replace with your value
composite_dispersion_instance = CompositeDispersion(effective_at=effective_at, dispersion_calculation=dispersion_calculation, variance=variance, first_quartile=first_quartile, third_quartile=third_quartile, range=range, constituents_in_scope=constituents_in_scope, constituents_excluded=constituents_excluded)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

