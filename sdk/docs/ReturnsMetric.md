# ReturnsMetric

Base class for a metric requested from the aggregated-returns (TWR) endpoint, measured over each period of  the grid (the grid granularity is set on the request via Period, not per metric). Polymorphic by type;  each supported type has a corresponding inherited class carrying the inputs only that metric takes.
## Example

```python
from lusid.models.returns_metric import ReturnsMetric
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

# Example with ReturnsMetric 

indicative_amount_metric_instance = lusid.models.indicative_amount_metric.IndicativeAmountMetric(
                        seed_amount = '', 
                        type = '', 
                        alias = '', )

returns_metric_instance = ReturnsMetric(indicative_amount_metric_instance)

```
See all compatible oneOf types with ReturnsMetric


 * [ReturnMetric](./ReturnMetric.md)

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

