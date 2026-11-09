# QualifyingInvestmentsHistory

The daily qualifying-investments history of one collective investment scheme and the flips within it.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**luid** | **str** | The LUSID instrument identifier of the collective investment scheme. | 
**threshold_percent** | **float** | The qualifying investments percentage the scheme must exceed to be a bond fund. | 
**observations** | [**List[QualifyingInvestmentsObservation]**](QualifyingInvestmentsObservation.md) | The daily qualifying investments observations in the requested window, oldest first. | 
**crossings** | [**List[QualifyingInvestmentsCrossing]**](QualifyingInvestmentsCrossing.md) | Each pair of consecutive observations where the bond fund result flipped. | 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.qualifying_investments_history import QualifyingInvestmentsHistory
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

href: Optional[StrictStr] = "example_href"
luid: StrictStr = "example_luid"
threshold_percent: Union[StrictFloat, StrictInt] = # Replace with your value
observations: List[QualifyingInvestmentsObservation] = # Replace with your value
crossings: List[QualifyingInvestmentsCrossing] = # Replace with your value
links: Optional[List[Link]] = None
qualifying_investments_history_instance = QualifyingInvestmentsHistory(href=href, luid=luid, threshold_percent=threshold_percent, observations=observations, crossings=crossings, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

