# ExternalDealingEstimateLine

One order within an external order set: a share class, a direction and either a number of units or an amount.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instrument_identifier_type** | **str** |  | 
**instrument_identifier** | **str** |  | 
**instrument_scope** | **str** |  | [optional] 
**trade_type** | **str** | Available values: Subscription, Redemption, SwitchOut, SwitchIn, TransferOut, TransferIn. | 
**units** | **float** |  | [optional] 
**amount** | [**ExternalDealingEstimateAmount**](ExternalDealingEstimateAmount.md) |  | [optional] 
## Example

```python
from lusid.models.external_dealing_estimate_line import ExternalDealingEstimateLine
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

instrument_identifier_type: StrictStr = "example_instrument_identifier_type"
instrument_identifier: StrictStr = "example_instrument_identifier"
instrument_scope: Optional[StrictStr] = "example_instrument_scope"
trade_type: StrictStr = "example_trade_type"
units: Optional[Union[StrictFloat, StrictInt]] = None
amount: Optional[ExternalDealingEstimateAmount] = None
external_dealing_estimate_line_instance = ExternalDealingEstimateLine(instrument_identifier_type=instrument_identifier_type, instrument_identifier=instrument_identifier, instrument_scope=instrument_scope, trade_type=trade_type, units=units, amount=amount)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

