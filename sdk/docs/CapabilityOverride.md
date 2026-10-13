# CapabilityOverride

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**capability** | **str** | Available values: RecallableDistributions, RecallCalls, ReturnOfExcessContributions, SubsequentCloseEqualisation, PartnerPnlAllocation, DistributionMechanism, DistributionCharacterSource, SecondaryTransfer, ExcuseExclude, DealScopedPnl, NettedCallAndDistribution. | 
**setting** | **str** | Available values: Allowed, Forbidden. | 
**reason** | **str** |  | [optional] 
## Example

```python
from lusid.models.capability_override import CapabilityOverride
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

capability: StrictStr = "example_capability"
setting: StrictStr = "example_setting"
reason: Optional[StrictStr] = "example_reason"
capability_override_instance = CapabilityOverride(capability=capability, setting=setting, reason=reason)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

