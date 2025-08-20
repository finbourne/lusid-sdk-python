# IrVolDependency

Economic dependency required to price interest rate products that contain optionality, for example swaptions. For example, can indicate a dependency on an IrVolCubeData.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency** | **str** | The domestic currency of the instrument declaring this dependency. | 
**vol_type** | **str** | Volatility type e.g. \&quot;LN\&quot; and \&quot;N\&quot; for log-normal and normal volatility. | 
**var_date** | **datetime** | The effectiveDate of the entity that this is a dependency for. Unless there is an obvious date this should be, like for a historic reset, then this is the valuation date. | 
**dependency_type** | **str** | The available values are: OpaqueDependency, CashDependency, DiscountingDependency, EquityCurveDependency, EquityVolDependency, FxDependency, FxForwardsDependency, FxVolDependency, IndexProjectionDependency, IrVolDependency, QuoteDependency, Vendor, CalendarDependency, InflationFixingDependency | 
## Example

```python
from lusid.models.ir_vol_dependency import IrVolDependency
from typing import Any, Dict
from pydantic.v1 import Field, StrictStr, constr, validator
from datetime import datetime
currency: StrictStr = "example_currency"
vol_type: StrictStr = "example_vol_type"
var_date: datetime = # Replace with your value
dependency_type: StrictStr = "example_dependency_type"
ir_vol_dependency_instance = IrVolDependency(currency=currency, vol_type=vol_type, var_date=var_date, dependency_type=dependency_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

