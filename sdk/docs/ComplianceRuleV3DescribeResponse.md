# ComplianceRuleV3DescribeResponse

A plain-English description of a V3 compliance rule. This is a minimal placeholder shape: the plain-English  generator is delivered separately, so the Lines property is currently empty and only the rule's identity  and subject are populated.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**subject** | **str** | Available values: Holdings, Orders. | [optional] 
**lines** | **List[str]** |  | [optional] 
## Example

```python
from lusid.models.compliance_rule_v3_describe_response import ComplianceRuleV3DescribeResponse
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

id: Optional[ResourceId] = None
subject: Optional[StrictStr] = "example_subject"
lines: Optional[List[StrictStr]] = None
compliance_rule_v3_describe_response_instance = ComplianceRuleV3DescribeResponse(id=id, subject=subject, lines=lines)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

