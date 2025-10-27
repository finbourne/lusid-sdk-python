# ComplianceRuleResultDetail

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rule_id** | [**ResourceId**](ResourceId.md) |  | 
**affected_portfolios_details** | [**List[ComplianceRuleResultPortfolioDetail]**](ComplianceRuleResultPortfolioDetail.md) |  | 
**affected_orders** | [**List[ResourceId]**](ResourceId.md) |  | 
**template_id** | [**ResourceId**](ResourceId.md) |  | 
**template_description** | **str** |  | 
**template_variation** | **str** |  | 
**status** | **str** |  | 
**rule_name** | **str** |  | 
**rule_description** | **str** |  | 
**outcome** | **str** |  | 
## Example

```python
from lusid.models.compliance_rule_result_detail import ComplianceRuleResultDetail
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

rule_id: ResourceId = # Replace with your value
affected_portfolios_details: List[ComplianceRuleResultPortfolioDetail] = # Replace with your value
affected_orders: List[ResourceId] = # Replace with your value
template_id: ResourceId = # Replace with your value
template_description: StrictStr = "example_template_description"
template_variation: StrictStr = "example_template_variation"
status: StrictStr = "example_status"
rule_name: StrictStr = "example_rule_name"
rule_description: StrictStr = "example_rule_description"
outcome: StrictStr = "example_outcome"
compliance_rule_result_detail_instance = ComplianceRuleResultDetail(rule_id=rule_id, affected_portfolios_details=affected_portfolios_details, affected_orders=affected_orders, template_id=template_id, template_description=template_description, template_variation=template_variation, status=status, rule_name=rule_name, rule_description=rule_description, outcome=outcome)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

