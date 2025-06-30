# EconomicDependency

Base class for representing economic dependencies.  Economic dependencies are a way of indicating how one concept depends upon another.  For example, when pricing an instrument with a particular model,  that model will declare that it has an EconomicDependency for each bit of market data  that it needs to complete the calculation.  Concretely, a pricing an FxForward will declare a dependency on the exchange rate between the two currencies  at the forward date.                Another example is when data is included in a data-structure only by reference.  Concretely, an object depending on a FlowConvention that is referenced only semantically via a FlowConventionName  will declare a FlowConventionDependency  so that the full data-structure of the referenced FlowConvention can be retrieved.                For deserialization purposes,  this class contains a discriminator EconomicDependencyType to indicate the derived type.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dependency_type** | **str** | The available values are: OpaqueDependency, CashDependency, DiscountingDependency, EquityCurveDependency, EquityVolDependency, FxDependency, FxForwardsDependency, FxVolDependency, IndexProjectionDependency, IrVolDependency, QuoteDependency, Vendor, CalendarDependency, InflationFixingDependency | 
## Example

```python
from lusid.models.economic_dependency import EconomicDependency
from typing import Any, Dict, Union
from pydantic.v1 import BaseModel, Field, StrictStr, validator

dependency_type: StrictStr = "example_dependency_type"
economic_dependency_instance = EconomicDependency(dependency_type=dependency_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

