# IgnoredDistributionTag

A distribution character tag the run did not pool by, on one account's lines.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gl_code** | **str** | The general ledger account of the tagged lines. | 
**line_count** | **int** | How many of the account&#39;s lines carried the ignored tag. | 
**amount** | **float** | The journal amount of the tagged lines, debits positive. | 
**reason** | **str** | Why the tag was ignored. Available values: NotPnlLine (the tagged line is not a profit and loss line, such as the cash leg of a tagged journal), CapabilityForbidden (the fund&#39;s DistributionCharacterSource capability is Forbidden, so characters come from buckets alone). | 
## Example

```python
from lusid.models.ignored_distribution_tag import IgnoredDistributionTag
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

gl_code: StrictStr = "example_gl_code"
line_count: StrictInt = # Replace with your value
line_count: StrictInt = 42
amount: Union[StrictFloat, StrictInt] = # Replace with your value
reason: StrictStr = "example_reason"
ignored_distribution_tag_instance = IgnoredDistributionTag(gl_code=gl_code, line_count=line_count, amount=amount, reason=reason)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

