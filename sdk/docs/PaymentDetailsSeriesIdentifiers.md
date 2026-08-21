# PaymentDetailsSeriesIdentifiers

The two hardcoded series identifier keys that uniquely identify a Payment Details data series.  The currency value must match the top-level currency field on the Payment Instruction.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_type** | **str** | The type of payment series. | 
**currency** | **str** | ISO 4217 currency code identifying the currency-specific series row. Must match the top-level currency field. | 
**custodian_account_scope** | **str** | Optional. The scope of the custodian account on the portfolio. Only permitted when the applicable entity is a Portfolio. | [optional] 
**custodian_account_code** | **str** | Optional. The code of the custodian account on the portfolio. Only permitted when the applicable entity is a Portfolio. | [optional] 
## Example

```python
from lusid.models.payment_details_series_identifiers import PaymentDetailsSeriesIdentifiers
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

payment_type: StrictStr = "example_payment_type"
currency: StrictStr = "example_currency"
custodian_account_scope: Optional[StrictStr] = "example_custodian_account_scope"
custodian_account_code: Optional[StrictStr] = "example_custodian_account_code"
payment_details_series_identifiers_instance = PaymentDetailsSeriesIdentifiers(payment_type=payment_type, currency=currency, custodian_account_scope=custodian_account_scope, custodian_account_code=custodian_account_code)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

