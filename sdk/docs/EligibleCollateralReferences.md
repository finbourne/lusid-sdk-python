# EligibleCollateralReferences

The eligible collateral schedule each party's posting is checked against.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**we_post** | [**ResourceId**](ResourceId.md) |  | [optional] 
**they_post** | [**ResourceId**](ResourceId.md) |  | [optional] 
## Example

```python
from lusid.models.eligible_collateral_references import EligibleCollateralReferences
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

we_post: Optional[ResourceId] = # Replace with your value
they_post: Optional[ResourceId] = # Replace with your value
eligible_collateral_references_instance = EligibleCollateralReferences(we_post=we_post, they_post=they_post)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

