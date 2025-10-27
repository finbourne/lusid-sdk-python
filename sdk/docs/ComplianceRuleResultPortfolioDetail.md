# ComplianceRuleResultPortfolioDetail

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ResourceId**](ResourceId.md) |  | 
**name** | **str** |  | 
## Example

```python
from lusid.models.compliance_rule_result_portfolio_detail import ComplianceRuleResultPortfolioDetail
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

id: ResourceId
name: StrictStr = "example_name"
compliance_rule_result_portfolio_detail_instance = ComplianceRuleResultPortfolioDetail(id=id, name=name)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

