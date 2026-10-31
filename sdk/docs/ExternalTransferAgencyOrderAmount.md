# ExternalTransferAgencyOrderAmount

A cash amount in a stated currency.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **float** |  | 
**currency** | **str** |  | 
## Example

```python
from lusid.models.external_transfer_agency_order_amount import ExternalTransferAgencyOrderAmount
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

value: Union[StrictFloat, StrictInt]
currency: StrictStr = "example_currency"
external_transfer_agency_order_amount_instance = ExternalTransferAgencyOrderAmount(value=value, currency=currency)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

