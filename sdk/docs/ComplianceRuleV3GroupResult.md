# ComplianceRuleV3GroupResult

The result of one rule for a single evaluated group: its status, the group key identifying it, the  measured value, the unit the value and limits are expressed in, the limits it was checked against, the  portfolios and orders it affects, and, when it could not be assessed, the missing-data details.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | Available values: Passed, Failed, Warning, MissingData. | [optional] 
**group_key** | **str** |  | [optional] 
**measured_value** | **float** |  | [optional] 
**hard_limit** | **float** |  | [optional] 
**soft_limit** | **float** |  | [optional] 
**unit** | **str** | Available values: Absolute, Percentage. | [optional] 
**affected_portfolio_ids** | **List[str]** |  | [optional] 
**affected_order_ids** | **List[str]** |  | [optional] 
**missing_data_details** | **List[str]** |  | [optional] 
## Example

```python
from lusid.models.compliance_rule_v3_group_result import ComplianceRuleV3GroupResult
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

status: Optional[StrictStr] = "example_status"
group_key: Optional[StrictStr] = "example_group_key"
measured_value: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
hard_limit: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
soft_limit: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
unit: Optional[StrictStr] = "example_unit"
affected_portfolio_ids: Optional[List[StrictStr]] = # Replace with your value
affected_order_ids: Optional[List[StrictStr]] = # Replace with your value
missing_data_details: Optional[List[StrictStr]] = # Replace with your value
compliance_rule_v3_group_result_instance = ComplianceRuleV3GroupResult(status=status, group_key=group_key, measured_value=measured_value, hard_limit=hard_limit, soft_limit=soft_limit, unit=unit, affected_portfolio_ids=affected_portfolio_ids, affected_order_ids=affected_order_ids, missing_data_details=missing_data_details)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

