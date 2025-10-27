# UpsertComplianceRuleRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ResourceId**](ResourceId.md) |  | 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**active** | **bool** |  | 
**template_id** | [**ResourceId**](ResourceId.md) |  | 
**variation** | **str** |  | 
**portfolio_group_id** | [**ResourceId**](ResourceId.md) |  | 
**parameters** | [**Dict[str, ComplianceParameter]**](ComplianceParameter.md) |  | 
**properties** | [**Dict[str, PerpetualProperty]**](PerpetualProperty.md) |  | 
## Example

```python
from lusid.models.upsert_compliance_rule_request import UpsertComplianceRuleRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

id: ResourceId
name: Optional[StrictStr] = "example_name"
description: Optional[StrictStr] = "example_description"
active: StrictBool
active:StrictBool = True
template_id: ResourceId = # Replace with your value
variation: StrictStr = "example_variation"
portfolio_group_id: ResourceId = # Replace with your value
parameters: Dict[str, ComplianceParameter]
properties: Dict[str, PerpetualProperty]
upsert_compliance_rule_request_instance = UpsertComplianceRuleRequest(id=id, name=name, description=description, active=active, template_id=template_id, variation=variation, portfolio_group_id=portfolio_group_id, parameters=parameters, properties=properties)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

