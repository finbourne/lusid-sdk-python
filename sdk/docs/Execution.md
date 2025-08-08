# Execution

The record of a number of executions against a single Placement (directly analogous to  a partial or full fill against a street order).
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ResourceId**](ResourceId.md) |  | 
**placement_id** | [**ResourceId**](ResourceId.md) |  | 
**properties** | [**Dict[str, PerpetualProperty]**](PerpetualProperty.md) | Client-defined properties associated with this execution. | [optional] 
**instrument_identifiers** | **Dict[str, str]** | The instrument ordered. | 
**lusid_instrument_id** | **str** | The LUSID instrument id for the instrument execution. | 
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
**version** | [**Version**](Version.md) |  | [optional] 
**data_model_membership** | [**DataModelMembership**](DataModelMembership.md) |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.execution import Execution
from typing import Any, Dict, List, Optional, Union
from pydantic.v1 import BaseModel, Field, StrictFloat, StrictInt, StrictStr, conlist, constr
from datetime import datetime
id: ResourceId = # Replace with your value
placement_id: ResourceId = # Replace with your value
properties: Optional[Dict[str, PerpetualProperty]] = # Replace with your value
instrument_identifiers: Dict[str, StrictStr] = # Replace with your value
lusid_instrument_id: StrictStr = "example_lusid_instrument_id"
quantity: Union[StrictFloat, StrictInt] = # Replace with your value
state: StrictStr = "example_state"
side: StrictStr = "example_side"
type: StrictStr = "example_type"
created_date: datetime = # Replace with your value
settlement_date: Optional[datetime] = # Replace with your value
price: CurrencyAndAmount = # Replace with your value
settlement_currency: StrictStr = "example_settlement_currency"
settlement_currency_fx_rate: Union[StrictFloat, StrictInt] = # Replace with your value
counterparty: StrictStr = "example_counterparty"
average_price: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
version: Optional[Version] = None
data_model_membership: Optional[DataModelMembership] = # Replace with your value
links: Optional[conlist(Link)] = None
execution_instance = Execution(id=id, placement_id=placement_id, properties=properties, instrument_identifiers=instrument_identifiers, lusid_instrument_id=lusid_instrument_id, quantity=quantity, state=state, side=side, type=type, created_date=created_date, settlement_date=settlement_date, price=price, settlement_currency=settlement_currency, settlement_currency_fx_rate=settlement_currency_fx_rate, counterparty=counterparty, average_price=average_price, version=version, data_model_membership=data_model_membership, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

