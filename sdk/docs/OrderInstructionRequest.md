# OrderInstructionRequest

A request to create or update a Order Instruction.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ResourceId**](ResourceId.md) |  | 
**created_date** | **datetime** | The active date of this order instruction. | 
**portfolio_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**instrument_identifiers** | **Dict[str, str]** | The instrument ordered. | [optional] 
**quantity** | **float** | The quantity of given instrument ordered. | [optional] 
**weight** | **float** | The proportion of the total portfolio value ordered for the given instrument ordered. | [optional] 
**price** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | [optional] 
**properties** | [**Dict[str, PerpetualProperty]**](PerpetualProperty.md) | Client-defined properties associated with this execution. | [optional] 
## Example

```python
from lusid.models.order_instruction_request import OrderInstructionRequest
from typing import Any, Dict, Optional, Union
from pydantic.v1 import BaseModel, Field, StrictFloat, StrictInt, StrictStr
from datetime import datetime
id: ResourceId = # Replace with your value
created_date: datetime = # Replace with your value
portfolio_id: Optional[ResourceId] = # Replace with your value
instrument_identifiers: Optional[Dict[str, StrictStr]] = # Replace with your value
quantity: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
weight: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
price: Optional[CurrencyAndAmount] = None
properties: Optional[Dict[str, PerpetualProperty]] = # Replace with your value
order_instruction_request_instance = OrderInstructionRequest(id=id, created_date=created_date, portfolio_id=portfolio_id, instrument_identifiers=instrument_identifiers, quantity=quantity, weight=weight, price=price, properties=properties)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

