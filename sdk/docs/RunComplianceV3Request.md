# RunComplianceV3Request

A request to run one or more V3 compliance rules against one or more individual portfolios, valuing  holdings with the supplied recipe. Each portfolio is evaluated on its own. The pre-trade variant  additionally includes each portfolio's live order flow.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rule_ids** | [**List[ResourceId]**](ResourceId.md) |  | 
**portfolio_ids** | [**List[ResourceId]**](ResourceId.md) |  | 
**recipe_id** | [**ResourceId**](ResourceId.md) |  | 
**effective_at** | **datetime** |  | [optional] 
**as_at** | **datetime** |  | [optional] 
## Example

```python
from lusid.models.run_compliance_v3_request import RunComplianceV3Request
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

rule_ids: List[ResourceId] = # Replace with your value
portfolio_ids: List[ResourceId] = # Replace with your value
recipe_id: ResourceId = # Replace with your value
effective_at: Optional[datetime] = # Replace with your value
as_at: Optional[datetime] = # Replace with your value
run_compliance_v3_request_instance = RunComplianceV3Request(rule_ids=rule_ids, portfolio_ids=portfolio_ids, recipe_id=recipe_id, effective_at=effective_at, as_at=as_at)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

