# CalendarDependency

For indicating a dependency upon calendar codes
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**calendars** | **List[str]** | The Codes of the calendars that are depended upon. | 
**dependency_type** | **str** | The available values are: OpaqueDependency, CashDependency, DiscountingDependency, EquityCurveDependency, EquityVolDependency, FxDependency, FxForwardsDependency, FxVolDependency, IndexProjectionDependency, IrVolDependency, QuoteDependency, Vendor, CalendarDependency, InflationFixingDependency | 
## Example

```python
from lusid.models.calendar_dependency import CalendarDependency
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

calendars: List[StrictStr] = # Replace with your value
dependency_type: StrictStr = "example_dependency_type"
calendar_dependency_instance = CalendarDependency(calendars=calendars, dependency_type=dependency_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

