# BondConversionSchedule

A BondConversionSchedule object represents a class containing the  information required for the creation of convertible features in a ComplexBond
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifiers** | **Dict[str, str]** | The market identifier(s) of the share that the bond converts to. The instrument  will not fail validation if no identifier is supplied. | [optional] 
**bond_conversion_entries** | [**List[BondConversionEntry]**](BondConversionEntry.md) | The dates at which the bond may be converted and associated information required about the conversion. | [optional] 
**conversion_trigger** | **str** | Corporate event that triggers a conversion    Supported string (enumeration) values are: [NextEquityFinancing, IpoConversion, KnownDates, SoftCall]. | 
**delivery_type** | **str** | Is a conversion made into cash or into shares?    Supported string (enumeration) values are: [Cash, Physical]. | [optional] 
**exercise_type** | **str** | The exercise type of the conversion schedule (American or European).  For American type, the bond is convertible from a given exercise date until the next date in the schedule, or until it matures.  For European type, the bond is only convertible on the given exercise date.    Supported string (enumeration) values are: [European, Bermudan, American]. | 
**includes_accrued** | **bool** | Set this to true if a accrued interest is included in the conversion. Defaults to true. | [optional] 
**mandatory_conversion** | **bool** | Set this to true if a conversion is mandatory if the trigger occurs. Defaults to false. | [optional] 
**notification_period_end** | **datetime** | The last day in the notification period for the conversion of the bond | [optional] 
**notification_period_start** | **datetime** | The first day in the notification period for the conversion of the bond | [optional] 
**schedule_type** | **str** | The available values are: FixedSchedule, FloatSchedule, OptionalitySchedule, StepSchedule, Exercise, FxRateSchedule, FxLinkedNotionalSchedule, BondConversionSchedule, Invalid | 
## Example

```python
from lusid.models.bond_conversion_schedule import BondConversionSchedule
from typing import Any, Dict, List, Optional
from pydantic.v1 import Field, StrictBool, StrictStr, conlist, constr, validator
from datetime import datetime
identifiers: Optional[Dict[str, StrictStr]] = # Replace with your value
bond_conversion_entries: Optional[conlist(BondConversionEntry)] = # Replace with your value
conversion_trigger: StrictStr = "example_conversion_trigger"
delivery_type: Optional[StrictStr] = "example_delivery_type"
exercise_type: StrictStr = "example_exercise_type"
includes_accrued: Optional[StrictBool] = # Replace with your value
includes_accrued:Optional[StrictBool] = None
mandatory_conversion: Optional[StrictBool] = # Replace with your value
mandatory_conversion:Optional[StrictBool] = None
notification_period_end: Optional[datetime] = # Replace with your value
notification_period_start: Optional[datetime] = # Replace with your value
schedule_type: StrictStr = "example_schedule_type"
bond_conversion_schedule_instance = BondConversionSchedule(identifiers=identifiers, bond_conversion_entries=bond_conversion_entries, conversion_trigger=conversion_trigger, delivery_type=delivery_type, exercise_type=exercise_type, includes_accrued=includes_accrued, mandatory_conversion=mandatory_conversion, notification_period_end=notification_period_end, notification_period_start=notification_period_start, schedule_type=schedule_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

