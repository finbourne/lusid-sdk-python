# FeeRuleUpsertResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | [**Dict[str, FeeRule]**](FeeRule.md) |  | 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.fee_rule_upsert_response import FeeRuleUpsertResponse
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, conlist

values: Dict[str, FeeRule] = # Replace with your value
links: Optional[conlist(Link)] = None
fee_rule_upsert_response_instance = FeeRuleUpsertResponse(values=values, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

