# PartnershipTypeCheckResult

The outcome of checking a fund's transaction types against the type contract of its partnership configuration  pack: the pack checked against and every type whose register balance deltas are not its contract.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pack** | [**PartnershipConfigPack**](PartnershipConfigPack.md) |  | 
**status** | **str** | The outcome of the check. Available values: Ok, Differences. | 
**differences** | [**List[PartnershipTypeDifference]**](PartnershipTypeDifference.md) | The transaction types whose register balance deltas are not their contract in the pack, whose movements book through a side the fund&#39;s transaction type scope does not define, or whose line legs lack the &#39;Registry&#39; movement option that books them into the registry; empty when the status is Ok. | 
## Example

```python
from lusid.models.partnership_type_check_result import PartnershipTypeCheckResult
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

pack: PartnershipConfigPack
status: StrictStr = "example_status"
differences: List[PartnershipTypeDifference] = # Replace with your value
partnership_type_check_result_instance = PartnershipTypeCheckResult(pack=pack, status=status, differences=differences)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

