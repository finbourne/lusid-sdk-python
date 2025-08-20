# EquityVolDependency

Economic dependency required to price Equity derivative products that contain optionality. Equity Vol surface is a grid of implied volatilities for an array of strikes and tenors, derived from vanilla option prices in the market.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | The code identifying the corresponding equity, e.g. US0378331005 if the MarketIdentifier was set to ISIN | 
**domestic_currency** | **str** | The domestic currency of the instrument declaring this dependency. | 
**vol_type** | **str** | Volatility type e.g. \&quot;LN\&quot; and \&quot;N\&quot; for log-normal and normal volatility. | 
**var_date** | **datetime** | The effectiveDate of the entity that this is a dependency for. Unless there is an obvious date this should be, like for a historic reset, then this is the valuation date. | 
**dependency_type** | **str** | The available values are: OpaqueDependency, CashDependency, DiscountingDependency, EquityCurveDependency, EquityVolDependency, FxDependency, FxForwardsDependency, FxVolDependency, IndexProjectionDependency, IrVolDependency, QuoteDependency, Vendor, CalendarDependency, InflationFixingDependency | 
## Example

```python
from lusid.models.equity_vol_dependency import EquityVolDependency
from typing import Any, Dict
from pydantic.v1 import Field, StrictStr, constr, validator
from datetime import datetime
code: StrictStr = "example_code"
domestic_currency: StrictStr = "example_domestic_currency"
vol_type: StrictStr = "example_vol_type"
var_date: datetime = # Replace with your value
dependency_type: StrictStr = "example_dependency_type"
equity_vol_dependency_instance = EquityVolDependency(code=code, domestic_currency=domestic_currency, vol_type=vol_type, var_date=var_date, dependency_type=dependency_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

