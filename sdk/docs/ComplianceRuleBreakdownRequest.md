# ComplianceRuleBreakdownRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_status** | **str** |  | 
**results_used** | **Dict[str, float]** |  | 
**properties_used** | **Dict[str, Optional[List[ModelProperty]]]** |  | 
**missing_data_information** | **List[str]** |  | 
**lineage** | [**List[LineageMember]**](LineageMember.md) |  | 
## Example

```python
from lusid.models.compliance_rule_breakdown_request import ComplianceRuleBreakdownRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

group_status: StrictStr = "example_group_status"
results_used: Dict[str, Union[StrictFloat, StrictInt]] = # Replace with your value
properties_used: Dict[str, Optional[List[ModelProperty]]] = # Replace with your value
missing_data_information: List[StrictStr] = # Replace with your value
lineage: List[LineageMember]
compliance_rule_breakdown_request_instance = ComplianceRuleBreakdownRequest(group_status=group_status, results_used=results_used, properties_used=properties_used, missing_data_information=missing_data_information, lineage=lineage)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

