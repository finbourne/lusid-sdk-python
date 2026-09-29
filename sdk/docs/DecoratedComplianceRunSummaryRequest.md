# DecoratedComplianceRunSummaryRequest

Specification for retrieving a decorated compliance run summary, optionally restricted to a  set of portfolios and/or portfolio groups.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**run_id** | [**ResourceId**](ResourceId.md) |  | 
**portfolio_entity_ids** | [**List[PortfolioEntityId]**](PortfolioEntityId.md) |  | [optional] 
**property_keys** | **List[str]** |  | [optional] 
## Example

```python
from lusid.models.decorated_compliance_run_summary_request import DecoratedComplianceRunSummaryRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

run_id: ResourceId = # Replace with your value
portfolio_entity_ids: Optional[List[PortfolioEntityId]] = # Replace with your value
property_keys: Optional[List[StrictStr]] = # Replace with your value
decorated_compliance_run_summary_request_instance = DecoratedComplianceRunSummaryRequest(run_id=run_id, portfolio_entity_ids=portfolio_entity_ids, property_keys=property_keys)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

