# TransferAgencyOrderEstimateResult

The estimated values for one order, together with the market facts they were struck from. The market facts  are repeated on every order priced against the same share class so that each result stands alone.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**most_recent_valuation_date** | **datetime** |  | [optional] 
**price_per_share** | **float** |  | [optional] 
**price_currency** | **str** |  | [optional] 
**estimated_units** | **float** |  | [optional] 
**estimated_amount** | **float** |  | [optional] 
**estimated_amount_currency** | **str** |  | [optional] 
**fx_rate_used** | **float** |  | [optional] 
## Example

```python
from lusid.models.transfer_agency_order_estimate_result import TransferAgencyOrderEstimateResult
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

order_id: Optional[ResourceId] = # Replace with your value
most_recent_valuation_date: Optional[datetime] = # Replace with your value
price_per_share: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
price_currency: Optional[StrictStr] = "example_price_currency"
estimated_units: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
estimated_amount: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
estimated_amount_currency: Optional[StrictStr] = "example_estimated_amount_currency"
fx_rate_used: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
transfer_agency_order_estimate_result_instance = TransferAgencyOrderEstimateResult(order_id=order_id, most_recent_valuation_date=most_recent_valuation_date, price_per_share=price_per_share, price_currency=price_currency, estimated_units=estimated_units, estimated_amount=estimated_amount, estimated_amount_currency=estimated_amount_currency, fx_rate_used=fx_rate_used)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

