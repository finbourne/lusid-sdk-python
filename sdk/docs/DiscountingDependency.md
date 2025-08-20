# DiscountingDependency

For indicating a dependency on discounting for a given currency. E.g Valuing a Bond with the Discounting model will declare a DiscountingDependency for the domestic currency of the bond to account for the time-value of the future cashFlows of the bond.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency** | **str** | The currency that needs to be discounted. | 
**var_date** | **datetime** | The effectiveDate of the entity that this is a dependency for. Unless there is an obvious date this should be, like for a historic reset, then this is the valuation date. | 
**dependency_type** | **str** | The available values are: OpaqueDependency, CashDependency, DiscountingDependency, EquityCurveDependency, EquityVolDependency, FxDependency, FxForwardsDependency, FxVolDependency, IndexProjectionDependency, IrVolDependency, QuoteDependency, Vendor, CalendarDependency, InflationFixingDependency | 
## Example

```python
from lusid.models.discounting_dependency import DiscountingDependency
from typing import Any, Dict
from pydantic.v1 import Field, StrictStr, validator
from datetime import datetime
currency: StrictStr = "example_currency"
var_date: datetime = # Replace with your value
dependency_type: StrictStr = "example_dependency_type"
discounting_dependency_instance = DiscountingDependency(currency=currency, var_date=var_date, dependency_type=dependency_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

