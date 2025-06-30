# InflationFixingDependency

For indicating a dependency upon an inflation fixing
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The Type of fixing (index, ratio or assumption) | 
**code** | **str** | The Code of the fixing, typically the index name | 
**var_date** | **datetime** | The effectiveAt of the inflation fixing | 
**dependency_type** | **str** | The available values are: OpaqueDependency, CashDependency, DiscountingDependency, EquityCurveDependency, EquityVolDependency, FxDependency, FxForwardsDependency, FxVolDependency, IndexProjectionDependency, IrVolDependency, QuoteDependency, Vendor, CalendarDependency, InflationFixingDependency | 
## Example

```python
from lusid.models.inflation_fixing_dependency import InflationFixingDependency
from typing import Any, Dict
from pydantic.v1 import Field, StrictStr, constr, validator
from datetime import datetime
type: StrictStr = "example_type"
code: StrictStr = "example_code"
var_date: datetime = # Replace with your value
dependency_type: StrictStr = "example_dependency_type"
inflation_fixing_dependency_instance = InflationFixingDependency(type=type, code=code, var_date=var_date, dependency_type=dependency_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

