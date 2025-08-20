# EquityCurveDependency

For indicating a dependency on an EquityCurve. E.g. When pricing an EquitySwap one may want to make predictions about the price of the underlying equity at future dates. If so, that model would declare an EquityCurve dependency so that it could obtain predictions from the EquityCurve.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**market_identifier** | **str** | Type of the code identifying the corresponding equity, e.g. ISIN or CUSIP | 
**code** | **str** | The code identifying the corresponding equity, e.g. US0378331005 if the MarketIdentifier was set to ISIN | 
**curve_type** | **str** | The curve type of the EquityCurve required. E.g. EquityCurveByPrices | 
**var_date** | **datetime** | The effectiveDate of the entity that this is a dependency for. Unless there is an obvious date this should be, like for a historic reset, then this is the valuation date. | 
**dependency_type** | **str** | The available values are: OpaqueDependency, CashDependency, DiscountingDependency, EquityCurveDependency, EquityVolDependency, FxDependency, FxForwardsDependency, FxVolDependency, IndexProjectionDependency, IrVolDependency, QuoteDependency, Vendor, CalendarDependency, InflationFixingDependency | 
## Example

```python
from lusid.models.equity_curve_dependency import EquityCurveDependency
from typing import Any, Dict
from pydantic.v1 import Field, StrictStr, constr, validator
from datetime import datetime
market_identifier: StrictStr = "example_market_identifier"
code: StrictStr = "example_code"
curve_type: StrictStr = "example_curve_type"
var_date: datetime = # Replace with your value
dependency_type: StrictStr = "example_dependency_type"
equity_curve_dependency_instance = EquityCurveDependency(market_identifier=market_identifier, code=code, curve_type=curve_type, var_date=var_date, dependency_type=dependency_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

