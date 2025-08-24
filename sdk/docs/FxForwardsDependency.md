# FxForwardsDependency

Indicates a dependency on an FxForwardCurve.  Identical to Fx dependencies in the meaning of domestic and foreign currencies, but describes a *set* of fx rates.  These rates are quoted rates for fx forwards, which can be used to interpolate the forward rate at a specific time in the future.  In the case of pips, the absolute rates can be expressed as rate = spotFx + pips / pipsPerUnit
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domestic_currency** | **str** | DomesticCurrency is the first currency in a currency pair quote e.g. eur-gbp, eur is the domestic currency. | 
**foreign_currency** | **str** | ForeignCurrency is the second currency in a currency pair quote e.g. eur-gbp, gbp is the foreign currency. | 
**curve_type** | **str** | Used to describe the format in which the curve is expressed  e.g. FxFwdCurve (general term to describe any representation), TenorFxFwdCurve, PipsFxFwdCurve. | 
**var_date** | **datetime** | The effectiveDate of the entity that this is a dependency for.  Unless there is an obvious date this should be, like for a historic reset, then this is the valuation date. | 
**dependency_type** | **str** | The available values are: OpaqueDependency, CashDependency, DiscountingDependency, EquityCurveDependency, EquityVolDependency, FxDependency, FxForwardsDependency, FxVolDependency, IndexProjectionDependency, IrVolDependency, QuoteDependency, Vendor, CalendarDependency, InflationFixingDependency | 
## Example

```python
from lusid.models.fx_forwards_dependency import FxForwardsDependency
from typing import Any, Dict
from pydantic.v1 import Field, StrictStr, constr, validator
from datetime import datetime
domestic_currency: StrictStr = "example_domestic_currency"
foreign_currency: StrictStr = "example_foreign_currency"
curve_type: StrictStr = "example_curve_type"
var_date: datetime = # Replace with your value
dependency_type: StrictStr = "example_dependency_type"
fx_forwards_dependency_instance = FxForwardsDependency(domestic_currency=domestic_currency, foreign_currency=foreign_currency, curve_type=curve_type, var_date=var_date, dependency_type=dependency_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

