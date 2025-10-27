# DecoratedComplianceRunSummary

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**run_id** | [**ResourceId**](ResourceId.md) |  | 
**details** | [**List[ComplianceRuleResultDetail]**](ComplianceRuleResultDetail.md) |  | 
## Example

```python
from lusid.models.decorated_compliance_run_summary import DecoratedComplianceRunSummary
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

run_id: ResourceId = # Replace with your value
details: List[ComplianceRuleResultDetail]
decorated_compliance_run_summary_instance = DecoratedComplianceRunSummary(run_id=run_id, details=details)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

