# OpenCloseMovementQueryParameters

The parameters of an open, close and movement report over a valuation point window.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start** | [**DateOrDiaryEntry**](DateOrDiaryEntry.md) |  | [optional] 
**end** | [**DateOrDiaryEntry**](DateOrDiaryEntry.md) |  | 
**variant** | **str** | Optional variant code. Only required when it is necessary to choose between scenarios with multiple estimates. | [optional] 
**sub_holding_keys_to_keep** | **List[str]** | The sub-holding keys to report separately, in the format {domain}/{scope}/{code}. Holdings of an instrument are consolidated to one row per holding type and currency across every other sub-holding key; with none kept every instrument is one row. | [optional] 
**instrument_property_keys** | **List[str]** | Property keys from the &#39;Instrument&#39; domain to decorate onto each row, in the format {domain}/{scope}/{code} e.g. &#39;Instrument/system/Name&#39;. | [optional] 
**opening_metrics** | **List[str]** | Valuation address keys to report at the opening of the window, e.g. &#39;Holding/Units&#39;, &#39;Quotes/Price&#39; or &#39;Valuation/PV&#39;. When holdings are consolidated a metric that scales with quantity is summed; any other is reported only when it is the same on every consolidated holding, and is otherwise null with a diagnostic in the row&#39;s errors. | [optional] 
**closing_metrics** | **List[str]** | Valuation address keys to report at the closing of the window, aggregated as the opening metrics are. | [optional] 
## Example

```python
from lusid.models.open_close_movement_query_parameters import OpenCloseMovementQueryParameters
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

start: Optional[DateOrDiaryEntry] = None
end: DateOrDiaryEntry
variant: Optional[StrictStr] = "example_variant"
sub_holding_keys_to_keep: Optional[List[StrictStr]] = # Replace with your value
instrument_property_keys: Optional[List[StrictStr]] = # Replace with your value
opening_metrics: Optional[List[StrictStr]] = # Replace with your value
closing_metrics: Optional[List[StrictStr]] = # Replace with your value
open_close_movement_query_parameters_instance = OpenCloseMovementQueryParameters(start=start, end=end, variant=variant, sub_holding_keys_to_keep=sub_holding_keys_to_keep, instrument_property_keys=instrument_property_keys, opening_metrics=opening_metrics, closing_metrics=closing_metrics)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

