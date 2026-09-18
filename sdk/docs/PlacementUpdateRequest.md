# PlacementUpdateRequest

A request to update a Placement.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ResourceId**](ResourceId.md) |  | 
**quantity** | **float** | The quantity of given instrument ordered. | [optional] 
**amount** | [**CurrencyAndAmount**](CurrencyAndAmount.md) |  | [optional] 
**properties** | [**Dict[str, PerpetualProperty]**](PerpetualProperty.md) | Client-defined properties associated with this placement. | [optional] 
**type** | **str** | Optionally changes the type of this placement (Market, Limit, Stop, StopLimit). A type may only be tightened: a Market placement may become Limit, Stop or StopLimit, and any placement may become StopLimit. A placement may be relaxed to Market only when the associated block is of type &#39;Market&#39;. Changing to a priced type requires a currency and the price(s) that type carries; a price the new type does not carry is cleared. Changing to Market clears both prices and may not be combined with a price update. A change to or from any other type is not subject to these rules, leaves both prices as they are, and is permitted only when the associated block is of type &#39;Market&#39;. | [optional] 
**limit_price** | **float** | Optionally updates the limit price of this placement, in the placement&#39;s limit price currency unless a currency is also specified. A currency is required if the placement has no limit price currency. | [optional] 
**stop_price** | **float** | Optionally updates the stop price of this placement, in the placement&#39;s stop price currency unless a currency is also specified. A currency is required if the placement has no stop price currency. | [optional] 
**counterparty** | **str** | Optionally specifies the market entity this placement is placed with. | [optional] 
**execution_system** | **str** | Optionally specifies the execution system in use. | [optional] 
**entry_type** | **str** | Optionally specifies the entry type of this placement. Available values: Undecided, Manual, Direct, Ems, External. | [optional] 
**currency** | **str** | The ISO currency code of the stop and/or limit price carried by the placement&#39;s type. Required when the type is changed to Stop, Limit or StopLimit, or when a price is set that the placement has no currency for; not permitted for a Market placement. For a value placement it must match the currency of the amount exactly, whether that amount is on the placement or in the update. | [optional] 
## Example

```python
from lusid.models.placement_update_request import PlacementUpdateRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

id: ResourceId
quantity: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
amount: Optional[CurrencyAndAmount] = None
properties: Optional[Dict[str, PerpetualProperty]] = # Replace with your value
type: Optional[StrictStr] = "example_type"
limit_price: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
stop_price: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
counterparty: Optional[StrictStr] = "example_counterparty"
execution_system: Optional[StrictStr] = "example_execution_system"
entry_type: Optional[StrictStr] = "example_entry_type"
currency: Optional[StrictStr] = "example_currency"
placement_update_request_instance = PlacementUpdateRequest(id=id, quantity=quantity, amount=amount, properties=properties, type=type, limit_price=limit_price, stop_price=stop_price, counterparty=counterparty, execution_system=execution_system, entry_type=entry_type, currency=currency)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

