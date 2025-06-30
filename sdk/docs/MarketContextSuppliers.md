# MarketContextSuppliers

It is possible to control which supplier is used for a given asset class.  This field is deprecated in favour of market data rules, which subsumes its functionality.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**commodity** | **str** |  | [optional] 
**credit** | **str** |  | [optional] 
**equity** | **str** |  | [optional] 
**fx** | **str** |  | [optional] 
**rates** | **str** |  | [optional] 
## Example

```python
from lusid.models.market_context_suppliers import MarketContextSuppliers
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, StrictStr

commodity: Optional[StrictStr] = "example_commodity"
credit: Optional[StrictStr] = "example_credit"
equity: Optional[StrictStr] = "example_equity"
fx: Optional[StrictStr] = "example_fx"
rates: Optional[StrictStr] = "example_rates"
market_context_suppliers_instance = MarketContextSuppliers(commodity=commodity, credit=credit, equity=equity, fx=fx, rates=rates)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

