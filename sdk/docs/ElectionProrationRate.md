# ElectionProrationRate

The proration rate the issuer applies to one option of a multi-option event, keyed by the option's election key.  An entry overrides the event-level proration rate for that election only.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**election_key** | **str** | The election key of the option this proration rate applies to. | 
**proration_rate** | **float** | The fraction of the quantity instructed on this option that the issuer accepts. Must be in (0, 1]. | 
## Example

```python
from lusid.models.election_proration_rate import ElectionProrationRate
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

election_key: StrictStr = "example_election_key"
proration_rate: Union[StrictFloat, StrictInt] = # Replace with your value
election_proration_rate_instance = ElectionProrationRate(election_key=election_key, proration_rate=proration_rate)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

