# ConsentAndExchangeElection

Election to both grant consent and exchange the holding (CEXC), at a given units ratio.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**election_key** | **str** | Unique key associated to this election. | 
**is_default** | **bool** | Is this election automatically applied in the absence of an election having been made.  May only be true for one election if multiple are provided. | [optional] 
**is_chosen** | **bool** | Is this the election that has been explicitly chosen from multiple options. | [optional] 
**units_ratio** | [**UnitsRatio**](UnitsRatio.md) |  | 
## Example

```python
from lusid.models.consent_and_exchange_election import ConsentAndExchangeElection
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

election_key: StrictStr = "example_election_key"
is_default: Optional[StrictBool] = # Replace with your value
is_default:Optional[StrictBool] = None
is_chosen: Optional[StrictBool] = # Replace with your value
is_chosen:Optional[StrictBool] = None
units_ratio: UnitsRatio = # Replace with your value
consent_and_exchange_election_instance = ConsentAndExchangeElection(election_key=election_key, is_default=is_default, is_chosen=is_chosen, units_ratio=units_ratio)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

