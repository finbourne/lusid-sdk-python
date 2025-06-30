# A2BMovementRecord

A2B Movement Record - shows A2B category based changes relating to a specific movement
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**portfolio_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**holding_type** | **str** | The code for the type of the holding e.g. P, B, C, R, F etc. | [optional] 
**instrument_scope** | **str** | The unique Lusid Instrument Id (LUID) of the instrument that the holding is in. | [optional] 
**instrument_uid** | **str** | The unique Lusid Instrument Id (LUID) of the instrument that the holding is in. | [optional] 
**sub_holding_keys** | [**Dict[str, PerpetualProperty]**](PerpetualProperty.md) | The sub-holding properties which identify the holding. Each property will be from the &#39;Transaction&#39; domain. These are configured on a transaction portfolio. | [optional] 
**currency** | **str** | The holding currency. | [optional] 
**transaction_id** | **str** | The unique identifier for the transaction. | [optional] 
**movement_name** | **str** | The name of the movement. | [optional] 
**effective_date** | **datetime** | The date of the movement. | [optional] 
**units** | **float** | The number of units of the instrument that are affected by the movement. | [optional] 
**start** | [**A2BCategory**](A2BCategory.md) |  | [optional] 
**flows** | [**A2BCategory**](A2BCategory.md) |  | [optional] 
**gains** | [**A2BCategory**](A2BCategory.md) |  | [optional] 
**carry** | [**A2BCategory**](A2BCategory.md) |  | [optional] 
**end** | [**A2BCategory**](A2BCategory.md) |  | [optional] 
**properties** | [**Dict[str, ModelProperty]**](ModelProperty.md) | The properties which have been requested to be decorated onto the holding. These will be from the &#39;Instrument&#39; domain. | [optional] 
**group_id** | **str** | Arbitrary string that can be used to cross reference an entry in the A2B report with activity in the A2B-Movements. This should be used purely as a token. The content should not be relied upon. | [optional] 
**errors** | [**List[ResponseMetaData]**](ResponseMetaData.md) | Any errors with the record are reported here. | [optional] 
## Example

```python
from lusid.models.a2_b_movement_record import A2BMovementRecord
from typing import Any, Dict, List, Optional, Union
from pydantic.v1 import BaseModel, Field, StrictFloat, StrictInt, StrictStr, conlist
from datetime import datetime
portfolio_id: Optional[ResourceId] = # Replace with your value
holding_type: Optional[StrictStr] = "example_holding_type"
instrument_scope: Optional[StrictStr] = "example_instrument_scope"
instrument_uid: Optional[StrictStr] = "example_instrument_uid"
sub_holding_keys: Optional[Dict[str, PerpetualProperty]] = # Replace with your value
currency: Optional[StrictStr] = "example_currency"
transaction_id: Optional[StrictStr] = "example_transaction_id"
movement_name: Optional[StrictStr] = "example_movement_name"
effective_date: Optional[datetime] = # Replace with your value
units: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
start: Optional[A2BCategory] = None
flows: Optional[A2BCategory] = None
gains: Optional[A2BCategory] = None
carry: Optional[A2BCategory] = None
end: Optional[A2BCategory] = None
properties: Optional[Dict[str, ModelProperty]] = # Replace with your value
group_id: Optional[StrictStr] = "example_group_id"
errors: Optional[conlist(ResponseMetaData)] = # Replace with your value
a2_b_movement_record_instance = A2BMovementRecord(portfolio_id=portfolio_id, holding_type=holding_type, instrument_scope=instrument_scope, instrument_uid=instrument_uid, sub_holding_keys=sub_holding_keys, currency=currency, transaction_id=transaction_id, movement_name=movement_name, effective_date=effective_date, units=units, start=start, flows=flows, gains=gains, carry=carry, end=end, properties=properties, group_id=group_id, errors=errors)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

