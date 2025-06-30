# ComplianceRule

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scope** | **str** |  | 
**code** | **str** |  | 
**display_name** | **str** |  | 
**type** | **str** |  | 
**property_key** | **str** |  | [optional] 
**value** | **str** |  | [optional] 
**address_key** | **str** |  | [optional] 
**lower_bound** | **float** |  | 
**upper_bound** | **float** |  | 
**schedule** | **str** |  | 
**hard_requirement** | **bool** |  | 
**target_portfolio_ids** | [**List[ResourceId]**](ResourceId.md) |  | 
**description** | **str** |  | [optional] 
**version** | [**Version**](Version.md) |  | [optional] 
## Example

```python
from lusid.models.compliance_rule import ComplianceRule
from typing import Any, Dict, List, Optional, Union
from pydantic.v1 import BaseModel, Field, StrictBool, StrictFloat, StrictInt, StrictStr, conlist, constr, validator

scope: StrictStr = "example_scope"
code: StrictStr = "example_code"
display_name: StrictStr = "example_display_name"
type: StrictStr = "example_type"
property_key: Optional[StrictStr] = "example_property_key"
value: Optional[StrictStr] = "example_value"
address_key: Optional[StrictStr] = "example_address_key"
lower_bound: Union[StrictFloat, StrictInt] = # Replace with your value
upper_bound: Union[StrictFloat, StrictInt] = # Replace with your value
schedule: StrictStr = "example_schedule"
hard_requirement: StrictBool = # Replace with your value
hard_requirement:StrictBool = True
target_portfolio_ids: conlist(ResourceId) = # Replace with your value
description: Optional[StrictStr] = "example_description"
version: Optional[Version] = None
compliance_rule_instance = ComplianceRule(scope=scope, code=code, display_name=display_name, type=type, property_key=property_key, value=value, address_key=address_key, lower_bound=lower_bound, upper_bound=upper_bound, schedule=schedule, hard_requirement=hard_requirement, target_portfolio_ids=target_portfolio_ids, description=description, version=version)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

