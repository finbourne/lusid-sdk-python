# ExecutionRequest

A request to create or update a Execution.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ResourceId**](ResourceId.md) |  | 
**placement_id** | [**ResourceId**](ResourceId.md) |  | 
**properties** | [**Dict[str, PerpetualProperty]**](PerpetualProperty.md) | Client-defined properties associated with this execution. | [optional] 
**instrument_identifiers** | **Dict[str, Optional[str]]** | The instrument ordered. | 
**quantity** | **float** | The quantity of given instrument ordered. | 
**state** | **str** | The state of this execution (typically a FIX state; Open, Filled, etc). | 
**side** | **str** | The side (Buy, Sell, ...) of this execution. | 
**type** | **str** | The type of this execution (Market, Limit, etc). | 
**created_date** | **datetime** | The active date of this execution. | 
**settlement_date** | **datetime** | The (optional) settlement date for this execution | [optional] 
**price** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | 
**settlement_currency** | **str** | The execution&#39;s settlement currency. | 
**settlement_currency_fx_rate** | **float** | The exectuion&#39;s settlement currency rate. | 
**counterparty** | **str** | The market entity this placement is placed with. | 
**average_price** | **float** | The average price of all executions for a given placement at the time of upsert | [optional] 
## Example

```python
from lusid.models.execution_request import ExecutionRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

id: ResourceId
placement_id: ResourceId = # Replace with your value
properties: Optional[Dict[str, PerpetualProperty]] = # Replace with your value
instrument_identifiers: Dict[str, Optional[StrictStr]] = # Replace with your value
quantity: Union[StrictFloat, StrictInt] = # Replace with your value
state: StrictStr = "example_state"
side: StrictStr = "example_side"
type: StrictStr = "example_type"
created_date: datetime = # Replace with your value
settlement_date: Optional[datetime] = # Replace with your value
price: CurrencyAndAmount
settlement_currency: StrictStr = "example_settlement_currency"
settlement_currency_fx_rate: Union[StrictFloat, StrictInt] = # Replace with your value
counterparty: StrictStr = "example_counterparty"
average_price: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
execution_request_instance = ExecutionRequest(id=id, placement_id=placement_id, properties=properties, instrument_identifiers=instrument_identifiers, quantity=quantity, state=state, side=side, type=type, created_date=created_date, settlement_date=settlement_date, price=price, settlement_currency=settlement_currency, settlement_currency_fx_rate=settlement_currency_fx_rate, counterparty=counterparty, average_price=average_price)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

