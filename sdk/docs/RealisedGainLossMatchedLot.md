# RealisedGainLossMatchedLot

The lot a realised chargeable-gains leg was matched against: its cost in the portfolio currency, the date of the  acquisition that opened it and its chargeable-gains role.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**original_cost** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | [optional] 
**purchase_date** | **datetime** |  | [optional] 
**role** | **str** | Available values: DayLot, Section104Pool, Holding1982, Holding1965, FutureAcquisition. | [optional] 
## Example

```python
from lusid.models.realised_gain_loss_matched_lot import RealisedGainLossMatchedLot
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

original_cost: Optional[CurrencyAndAmount] = # Replace with your value
purchase_date: Optional[datetime] = # Replace with your value
role: Optional[StrictStr] = "example_role"
realised_gain_loss_matched_lot_instance = RealisedGainLossMatchedLot(original_cost=original_cost, purchase_date=purchase_date, role=role)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

