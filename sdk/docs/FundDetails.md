# FundDetails

The details of a Fund.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency** | **str** | The currency of the fund which is the same as the base currency of all the portfolios of the fund&#39;s Abor. | [optional] 
**pricing_basis** | **str** | The side of the quote the NAV type valued the fund on: Mid, Bid or Ask. Absent when the NAV type defers to the valuation recipe&#39;s own pricing basis. When the NAV type has a swing pricing rule this is the basis the rule applied. | [optional] 
**swing_pricing** | [**SwingPricingDecision**](SwingPricingDecision.md) |  | [optional] 
## Example

```python
from lusid.models.fund_details import FundDetails
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

currency: Optional[StrictStr] = "example_currency"
pricing_basis: Optional[StrictStr] = "example_pricing_basis"
swing_pricing: Optional[SwingPricingDecision] = # Replace with your value
fund_details_instance = FundDetails(currency=currency, pricing_basis=pricing_basis, swing_pricing=swing_pricing)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

