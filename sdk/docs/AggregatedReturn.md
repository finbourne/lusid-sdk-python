# AggregatedReturn

A list of Aggregated Returns.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**effective_at** | **datetime** | The effectiveAt for the return. | 
**end_of_period** | **datetime** | The end of period date. For the monthly period this will be the Month End Date. | 
**opening_market_value** | **float** | The opening market value. | [optional] 
**closing_market_value** | **float** | The closing market value. | [optional] 
**metrics_value** | **Dict[str, float]** | The value for the specified metric. | 
**frequency** | **str** | Show the aggregated output returns on a Daily or Monthly period. | [optional] 
**composite_members** | **int** | The number of members in the Composite on the given day. | [optional] 
**composite_members_without_return** | [**List[ResourceId]**](ResourceId.md) | List containing Composite members which post no return on the given day. | [optional] 
**warnings** | **List[str]** | List of the warnings about the calculation of the aggregated return. | [optional] 
## Example

```python
from lusid.models.aggregated_return import AggregatedReturn
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

effective_at: datetime = # Replace with your value
end_of_period: datetime = # Replace with your value
opening_market_value: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
closing_market_value: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
metrics_value: Dict[str, Union[StrictFloat, StrictInt]] = # Replace with your value
frequency: Optional[StrictStr] = "example_frequency"
composite_members: Optional[StrictInt] = # Replace with your value
composite_members: Optional[StrictInt] = None
composite_members_without_return: Optional[List[ResourceId]] = # Replace with your value
warnings: Optional[List[StrictStr]] = # Replace with your value
aggregated_return_instance = AggregatedReturn(effective_at=effective_at, end_of_period=end_of_period, opening_market_value=opening_market_value, closing_market_value=closing_market_value, metrics_value=metrics_value, frequency=frequency, composite_members=composite_members, composite_members_without_return=composite_members_without_return, warnings=warnings)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

