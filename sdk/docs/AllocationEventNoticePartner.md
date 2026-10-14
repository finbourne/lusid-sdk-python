# AllocationEventNoticePartner

The partner a notice is addressed to.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**investor_record_id** | **str** | The investor record identifier of the partner. | 
**display_name** | **str** | The display name of the partner. | [optional] 
**commitment** | **float** | The partner&#39;s total commitment. | 
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
allocation_event_notice_partner_instance = AllocationEventNoticePartner(investor_record_id=investor_record_id, display_name=display_name, commitment=commitment)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

