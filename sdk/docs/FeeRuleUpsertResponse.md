# FeeRuleUpsertResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | [**Dict[str, FeeRule]**](FeeRule.md) |  | 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.fee_rule_upsert_response import FeeRuleUpsertResponse
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

values: Dict[str, FeeRule]
links: Optional[List[Link]] = None
fee_rule_upsert_response_instance = FeeRuleUpsertResponse(values=values, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

