# FundDetails

The details of a Fund.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency** | **str** | The currency of the fund which is the same as the base currency of all the portfolios of the fund&#39;s Abor. | [optional] 
## Example

```python
from lusid.models.fund_details import FundDetails
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, StrictStr

currency: Optional[StrictStr] = "example_currency"
fund_details_instance = FundDetails(currency=currency)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

