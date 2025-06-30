# ComplianceRuleResultPortfolioDetail

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ResourceId**](ResourceId.md) |  | 
**name** | **str** |  | 
## Example

```python
from lusid.models.compliance_rule_result_portfolio_detail import ComplianceRuleResultPortfolioDetail
from typing import Any, Dict
from pydantic.v1 import BaseModel, Field, constr

id: ResourceId = # Replace with your value
name: StrictStr = "example_name"
compliance_rule_result_portfolio_detail_instance = ComplianceRuleResultPortfolioDetail(id=id, name=name)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

