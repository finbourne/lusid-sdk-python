# ComplianceRuleUpsertRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scope** | **str** |  | 
**code** | **str** |  | [optional] 
**display_name** | **str** |  | [optional] 
**type** | **str** |  | 
**property_key** | **str** |  | [optional] 
**value** | **str** |  | [optional] 
**lower_bound** | **float** |  | 
**upper_bound** | **float** |  | 
**schedule** | **str** |  | 
**hard_requirement** | **bool** |  | 
**target_portfolio_ids** | [**List[ResourceId]**](ResourceId.md) |  | 
**description** | **str** |  | [optional] 
**address_key** | **str** |  | [optional] 
## Example

```python
from lusid.models.compliance_rule_upsert_request import ComplianceRuleUpsertRequest
from typing import Any, Dict, List, Optional, Union
from pydantic.v1 import BaseModel, Field, StrictBool, StrictFloat, StrictInt, StrictStr, conlist, constr, validator

scope: StrictStr = "example_scope"
code: Optional[StrictStr] = "example_code"
display_name: Optional[StrictStr] = "example_display_name"
type: StrictStr = "example_type"
property_key: Optional[StrictStr] = "example_property_key"
value: Optional[StrictStr] = "example_value"
lower_bound: Union[StrictFloat, StrictInt] = # Replace with your value
upper_bound: Union[StrictFloat, StrictInt] = # Replace with your value
schedule: StrictStr = "example_schedule"
hard_requirement: StrictBool = # Replace with your value
hard_requirement:StrictBool = True
target_portfolio_ids: conlist(ResourceId) = # Replace with your value
description: Optional[StrictStr] = "example_description"
address_key: Optional[StrictStr] = "example_address_key"
compliance_rule_upsert_request_instance = ComplianceRuleUpsertRequest(scope=scope, code=code, display_name=display_name, type=type, property_key=property_key, value=value, lower_bound=lower_bound, upper_bound=upper_bound, schedule=schedule, hard_requirement=hard_requirement, target_portfolio_ids=target_portfolio_ids, description=description, address_key=address_key)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

