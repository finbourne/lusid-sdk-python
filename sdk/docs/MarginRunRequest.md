# MarginRunRequest

A request to value collateral agreements for a business date and publish their margin calls.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**effective_at** | **str** | The business date, datetime or cut label to value the agreements at. | 
**as_at** | **datetime** | The asAt datetime to read agreements, portfolios and market data at. Defaults to the current LUSID system datetime if not specified. | [optional] 
**agreement_filter** | **str** | An expression selecting the collateral agreements to run, in the same syntax as listing collateral agreements. Every agreement the caller may calculate margin for is run if not specified. | [optional] 
**scenario** | [**ResourceId**](ResourceId.md) |  | [optional] 
## Example

```python
from lusid.models.margin_run_request import MarginRunRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

effective_at: StrictStr = "example_effective_at"
as_at: Optional[datetime] = # Replace with your value
agreement_filter: Optional[StrictStr] = "example_agreement_filter"
scenario: Optional[ResourceId] = None
margin_run_request_instance = MarginRunRequest(effective_at=effective_at, as_at=as_at, agreement_filter=agreement_filter, scenario=scenario)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

