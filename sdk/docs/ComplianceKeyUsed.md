# ComplianceKeyUsed

A key a holding contributed to the rule: the key, the role(s) it played in the rule, the holding's own value for  it, and which bag the value was read from.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | 
**roles** | **List[str]** |  | 
**value** | **object** | This holding&#39;s own value for the key. Polymorphic: a number for a result or metric property, a label string for  a label property, or a string for a related property. | [optional] 
**source** | **str** |  | 
## Example

```python
from lusid.models.compliance_key_used import ComplianceKeyUsed
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

key: StrictStr = "example_key"
roles: List[StrictStr]
value: Optional[Any] = # Replace with your value
source: StrictStr = "example_source"
compliance_key_used_instance = ComplianceKeyUsed(key=key, roles=roles, value=value, source=source)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

