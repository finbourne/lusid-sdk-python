# OpenCloseMovementRecord

One row of the open, close and movement report: the net asset economic buckets at the opening and closing  of the window, the period's movements by economic bucket, and the requested valuation metrics and  instrument properties, per instrument or per kept sub-holding key.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**portfolio_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**holding_type** | **str** | The code for the type of the holding e.g. P, B, C, R, F etc. | [optional] 
**instrument_scope** | **str** | The unique Lusid Instrument Id (LUID) of the instrument that the holding is in. | [optional] 
**instrument_uid** | **str** | The unique Lusid Instrument Id (LUID) of the instrument that the holding is in. | [optional] 
**sub_holding_keys** | [**Dict[str, PerpetualProperty]**](PerpetualProperty.md) | The values of the sub-holding keys the request kept separate. Empty when the row is consolidated to the instrument. | [optional] 
**currency** | **str** | The holding currency. | [optional] 
**opening** | [**List[EconomicBucketAmount]**](EconomicBucketAmount.md) | The net asset economic buckets at the opening of the window, from the opening valuation. Empty when nothing was held. Amounts follow the journal entry line sign convention: a long position&#39;s balances are positive. Note that the A2B report&#39;s signs are the opposite for gains. | [optional] 
**closing** | [**List[EconomicBucketAmount]**](EconomicBucketAmount.md) | The net asset economic buckets at the closing of the window, from the closing valuation. Empty when nothing is held. Signs as for the opening. | [optional] 
**movements** | [**List[EconomicBucketAmount]**](EconomicBucketAmount.md) | The period&#39;s movements by economic bucket, component and variant, classified exactly as the journal entry lines classify them: the transaction lines of the window (cost flows in the NA buckets, carry, fees and realised gains in the PL buckets) plus the remeasurement of each net asset bucket between the two valuations, booked to its PL bucket. Signs follow the journal entry line convention, so income and gains are negative. The row reconciles as: closing &#x3D; opening + movements in NA buckets - movements in the remeasurement buckets (PL_UnrealPriceGL, PL_UnrealFXGL, PL_Accrued, PL_UnrealisedAmortised, PL_PIKAccrued, PL_DelayedCompensation); any residual is booked to PL_Rounding. | [optional] 
**opening_metrics** | **Dict[str, Optional[float]]** | The requested valuation metrics at the opening of the window, keyed by address key. Absent when nothing was held; null where the metric is unavailable or differs across the consolidated holdings. | [optional] 
**closing_metrics** | **Dict[str, Optional[float]]** | The requested valuation metrics at the closing of the window, keyed by address key, as the opening metrics. | [optional] 
**properties** | [**Dict[str, ModelProperty]**](ModelProperty.md) | The properties which have been requested to be decorated onto the holding. These will be from the &#39;Instrument&#39; domain. | [optional] 
**errors** | [**List[ResponseMetaData]**](ResponseMetaData.md) | Any errors with the row are reported here, including metrics that could not be consolidated and reconciliation residuals beyond rounding. | [optional] 
## Example

```python
from lusid.models.open_close_movement_record import OpenCloseMovementRecord
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

portfolio_id: Optional[ResourceId] = # Replace with your value
holding_type: Optional[StrictStr] = "example_holding_type"
instrument_scope: Optional[StrictStr] = "example_instrument_scope"
instrument_uid: Optional[StrictStr] = "example_instrument_uid"
sub_holding_keys: Optional[Dict[str, PerpetualProperty]] = # Replace with your value
currency: Optional[StrictStr] = "example_currency"
opening: Optional[List[EconomicBucketAmount]] = # Replace with your value
closing: Optional[List[EconomicBucketAmount]] = # Replace with your value
movements: Optional[List[EconomicBucketAmount]] = # Replace with your value
opening_metrics: Optional[Dict[str, Optional[Union[StrictFloat, StrictInt]]]] = # Replace with your value
closing_metrics: Optional[Dict[str, Optional[Union[StrictFloat, StrictInt]]]] = # Replace with your value
properties: Optional[Dict[str, ModelProperty]] = # Replace with your value
errors: Optional[List[ResponseMetaData]] = # Replace with your value
open_close_movement_record_instance = OpenCloseMovementRecord(portfolio_id=portfolio_id, holding_type=holding_type, instrument_scope=instrument_scope, instrument_uid=instrument_uid, sub_holding_keys=sub_holding_keys, currency=currency, opening=opening, closing=closing, movements=movements, opening_metrics=opening_metrics, closing_metrics=closing_metrics, properties=properties, errors=errors)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

