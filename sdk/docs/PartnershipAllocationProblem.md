# PartnershipAllocationProblem

Why the period cannot be allocated to the partners as it stands. The read reports it; the allocation run and the  acceptance refuse with the same failure.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | The problem. Available values: AllocationRulesNotConfigured, UnbucketedPnl, UnknownDistributionCharacter. | 
**message** | **str** | What is wrong and what to change, naming the accounts, amounts and values concerned. | 
## Example

```python
from lusid.models.partnership_allocation_problem import PartnershipAllocationProblem
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

code: StrictStr = "example_code"
message: StrictStr = "example_message"
partnership_allocation_problem_instance = PartnershipAllocationProblem(code=code, message=message)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

