# HoldingEntitlementsResponse

The holding entitlements that were upserted, and the failures for those that could not be.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | [**Dict[str, HoldingEntitlement]**](HoldingEntitlement.md) | The collection of successfully upserted entitlements | [optional] 
**failed** | [**Dict[str, ErrorDetail]**](ErrorDetail.md) | The collection of error information for entitlements that could not be upserted | [optional] 
## Example

```python
from lusid.models.holding_entitlements_response import HoldingEntitlementsResponse
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

values: Optional[Dict[str, HoldingEntitlement]] = # Replace with your value
failed: Optional[Dict[str, ErrorDetail]] = # Replace with your value
holding_entitlements_response_instance = HoldingEntitlementsResponse(values=values, failed=failed)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

