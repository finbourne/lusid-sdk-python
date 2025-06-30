# InstrumentResolutionDetail

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instrument_identifiers** | **Dict[str, str]** | Unique instrument identifiers | 
**lusid_instrument_id** | **str** | LUSID&#39;s internal unique instrument identifier, resolved from the instrument identifiers | [optional] [readonly] 
**instrument_scope** | **str** | The scope in which the instrument lies. | [optional] [readonly] 
**launch_price** | **float** | The launch price set when a shareclass is added to the fund. Defaults to 1. | [optional] 
**launch_date** | **datetime** | The launch date set when a shareclass is added to the fund. Defaults to Fund Inception Date. | [optional] 
## Example

```python
from lusid.models.instrument_resolution_detail import InstrumentResolutionDetail
from typing import Any, Dict, Optional, Union
from pydantic.v1 import BaseModel, Field, StrictFloat, StrictInt, StrictStr, constr, validator
from datetime import datetime
instrument_identifiers: Dict[str, StrictStr] = # Replace with your value
lusid_instrument_id: Optional[StrictStr] = "example_lusid_instrument_id"
instrument_scope: Optional[StrictStr] = "example_instrument_scope"
launch_price: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
launch_date: Optional[datetime] = # Replace with your value
instrument_resolution_detail_instance = InstrumentResolutionDetail(instrument_identifiers=instrument_identifiers, lusid_instrument_id=lusid_instrument_id, instrument_scope=instrument_scope, launch_price=launch_price, launch_date=launch_date)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

