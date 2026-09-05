# TransferAgencyOrderToEstimate

The values of an order to estimate, for an order that has not been saved yet or whose values are being  changed. Carries only what the estimate reads - it is not a whole order and cannot be used to create one.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**portfolio_id** | [**ResourceId**](ResourceId.md) |  | 
**instrument_identifier_type** | **str** |  | 
**instrument_identifier** | **str** |  | 
**instrument_scope** | **str** |  | [optional] 
**transaction_category** | **str** | Available values: Subscription, Redemption, SwitchOut, SwitchIn, TransferOut, TransferIn. | [optional] 
**currency** | **str** |  | 
**quantity** | **float** |  | [optional] 
**amount** | **float** |  | [optional] 
**weight** | **float** |  | [optional] 
**transaction_date** | **datetime** |  | [optional] 
**exchange_rate** | **float** |  | [optional] 
## Example

```python
from lusid.models.transfer_agency_order_to_estimate import TransferAgencyOrderToEstimate
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

portfolio_id: ResourceId = # Replace with your value
instrument_identifier_type: StrictStr = "example_instrument_identifier_type"
instrument_identifier: StrictStr = "example_instrument_identifier"
instrument_scope: Optional[StrictStr] = "example_instrument_scope"
transaction_category: Optional[StrictStr] = "example_transaction_category"
currency: StrictStr = "example_currency"
quantity: Optional[Union[StrictFloat, StrictInt]] = None
amount: Optional[Union[StrictFloat, StrictInt]] = None
weight: Optional[Union[StrictFloat, StrictInt]] = None
transaction_date: Optional[datetime] = # Replace with your value
exchange_rate: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
transfer_agency_order_to_estimate_instance = TransferAgencyOrderToEstimate(portfolio_id=portfolio_id, instrument_identifier_type=instrument_identifier_type, instrument_identifier=instrument_identifier, instrument_scope=instrument_scope, transaction_category=transaction_category, currency=currency, quantity=quantity, amount=amount, weight=weight, transaction_date=transaction_date, exchange_rate=exchange_rate)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

