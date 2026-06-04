# CashOfferConstituent

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offer_price** | **float** |  | 
**currency** | **str** |  | 
**settlement_date** | **datetime** |  | 
**min_piece_size** | **float** |  | [optional] 
**min_increment** | **float** |  | [optional] 
## Example

```python
from lusid.models.cash_offer_constituent import CashOfferConstituent
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

offer_price: Union[StrictFloat, StrictInt] = # Replace with your value
currency: StrictStr = "example_currency"
settlement_date: datetime = # Replace with your value
min_piece_size: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
min_increment: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
cash_offer_constituent_instance = CashOfferConstituent(offer_price=offer_price, currency=currency, settlement_date=settlement_date, min_piece_size=min_piece_size, min_increment=min_increment)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

