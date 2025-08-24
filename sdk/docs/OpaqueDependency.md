# OpaqueDependency

Represents a dependency that could not be understood as an externally exposed dependency.  If this is an unexpected dependency, then please contact support.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dependency_type** | **str** | The available values are: OpaqueDependency, CashDependency, DiscountingDependency, EquityCurveDependency, EquityVolDependency, FxDependency, FxForwardsDependency, FxVolDependency, IndexProjectionDependency, IrVolDependency, QuoteDependency, Vendor, CalendarDependency, InflationFixingDependency | 
## Example

```python
from lusid.models.opaque_dependency import OpaqueDependency
from typing import Any, Dict
from pydantic.v1 import Field, StrictStr, validator

dependency_type: StrictStr = "example_dependency_type"
opaque_dependency_instance = OpaqueDependency(dependency_type=dependency_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

