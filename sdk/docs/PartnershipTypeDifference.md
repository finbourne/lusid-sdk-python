# PartnershipTypeDifference

A transaction type a fund's portfolios resolve whose register deltas are not its contract, whose sides its scope does not define, or whose line legs lack the option that books them into the registry.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | **str** | The source the transaction type is defined in. | 
**type** | **str** | The transaction type. | 
**scope** | **str** | The transaction type scope the fund&#39;s portfolio resolves the type in. | 
**expected** | [**List[PackRegisterDelta]**](PackRegisterDelta.md) | The register balance deltas the pack&#39;s contract expects of the type. | 
**actual** | [**List[RegisterDeltaMovement]**](RegisterDeltaMovement.md) | The register balance deltas the type&#39;s movements carry, each named by its movement. | 
**missing_sides** | **List[str]** | The sides the type&#39;s movements book through that the fund&#39;s transaction type scope does not define, so the type cannot be booked there; empty when every side is defined. | 
**missing_options** | [**List[MissingMovementOption]**](MissingMovementOption.md) | The movement options the type&#39;s line legs must carry to book the register and do not, each named by its movement. A leg that moves a register balance, or books the line&#39;s units and cost, without the &#39;Registry&#39; option books into the portfolio&#39;s holdings, where the register never looks; empty when every line leg carries it. | 
## Example

```python
from lusid.models.partnership_type_difference import PartnershipTypeDifference
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

source: StrictStr = "example_source"
type: StrictStr = "example_type"
scope: StrictStr = "example_scope"
expected: List[PackRegisterDelta] = # Replace with your value
actual: List[RegisterDeltaMovement] = # Replace with your value
missing_sides: List[StrictStr] = # Replace with your value
missing_options: List[MissingMovementOption] = # Replace with your value
partnership_type_difference_instance = PartnershipTypeDifference(source=source, type=type, scope=scope, expected=expected, actual=actual, missing_sides=missing_sides, missing_options=missing_options)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

