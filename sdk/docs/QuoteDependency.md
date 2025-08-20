# QuoteDependency

For indicating a dependency on the value of an asset at a point in time. If the time is omitted, then the dependency is interpreted as the latest value with respect to anything observing it. E.g. An EquitySwap will declare a dependency on the current price of the underlying equity.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**market_identifier** | **str** | Type of the code identifying the asset, e.g. ISIN or CUSIP | 
**code** | **str** | The code identifying the corresponding equity, e.g. US0378331005 if the MarketIdentifier was set to ISIN | 
**var_date** | **datetime** | The effectiveAt of the quote for the identified entity. | 
**dependency_type** | **str** | The available values are: OpaqueDependency, CashDependency, DiscountingDependency, EquityCurveDependency, EquityVolDependency, FxDependency, FxForwardsDependency, FxVolDependency, IndexProjectionDependency, IrVolDependency, QuoteDependency, Vendor, CalendarDependency, InflationFixingDependency | 
## Example

```python
from lusid.models.quote_dependency import QuoteDependency
from typing import Any, Dict
from pydantic.v1 import Field, StrictStr, constr, validator
from datetime import datetime
market_identifier: StrictStr = "example_market_identifier"
code: StrictStr = "example_code"
var_date: datetime = # Replace with your value
dependency_type: StrictStr = "example_dependency_type"
quote_dependency_instance = QuoteDependency(market_identifier=market_identifier, code=code, var_date=var_date, dependency_type=dependency_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

