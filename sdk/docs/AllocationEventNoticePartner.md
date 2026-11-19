# AllocationEventNoticePartner

The partner a notice is addressed to.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**investor_record_id** | **str** | The investor record identifier of the partner. | 
**display_name** | **str** | The display name of the partner. | [optional] 
**commitment** | **float** | The partner&#39;s committed capital on the fund the event allocates over at the event date, summed over the lines the event allocates to there; for a partner looked through to, its line on the feeder. Never the partner&#39;s total across funds. | 
**lines** | [**List[AllocationEventNoticePartnerLine]**](AllocationEventNoticePartnerLine.md) | The register lines the partner was allocated on, one per line, each with the fund whose register holds it, its commitment at the event date and the partner&#39;s share landing on it. The shares sum to the net amount due before tax withheld. | [optional] 
## Example

```python
from lusid.models.allocation_event_notice_partner import AllocationEventNoticePartner
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

investor_record_id: StrictStr = "example_investor_record_id"
display_name: Optional[StrictStr] = "example_display_name"
commitment: Union[StrictFloat, StrictInt] = # Replace with your value
lines: Optional[List[AllocationEventNoticePartnerLine]] = # Replace with your value
allocation_event_notice_partner_instance = AllocationEventNoticePartner(investor_record_id=investor_record_id, display_name=display_name, commitment=commitment, lines=lines)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

