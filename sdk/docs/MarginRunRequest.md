# MarginRunRequest

A request to value collateral agreements for a business date and publish their margin calls.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**effective_at** | **str** | The business date, datetime or cut label to value the agreements at. With an effectiveFrom, the last date of the span. | 
**as_at** | **datetime** | The asAt datetime to read agreements, portfolios and market data at. Defaults to the current LUSID system datetime if not specified. | [optional] 
**agreement_filter** | **str** | An expression selecting the collateral agreements to run, in the same syntax as listing collateral agreements. Every agreement the caller may calculate margin for is run if not specified. | [optional] 
**scenarios** | [**List[ResourceId]**](ResourceId.md) | The stored scenarios to value the agreements under, each as a what-if beside the base market, which the run always values. A scenario&#39;s calls are served beside the base calls only when asked for, and cannot be accepted, disputed or matched to a counterparty demand. At most 20. Only the base market is valued if not specified. | [optional] 
**effective_from** | **str** | The first business date, datetime or cut label of a span ending at effectiveAt. Each weekday from it to effectiveAt is valued as a run of its own, all at the same asAt, and a date after the asAt is a projection valued on the market as at the asAt that cannot be accepted, disputed or matched to a counterparty demand. At most 130 weekdays. Only effectiveAt is valued if not specified. | [optional] 
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
scenarios: Optional[List[ResourceId]] = # Replace with your value
effective_from: Optional[StrictStr] = "example_effective_from"
margin_run_request_instance = MarginRunRequest(effective_at=effective_at, as_at=as_at, agreement_filter=agreement_filter, scenarios=scenarios, effective_from=effective_from)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

