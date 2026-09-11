# ConsentGrantedElection

Election to grant consent to the proposed action (CONY), optionally in return for a consent fee.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**election_key** | **str** | Unique key associated to this election. | 
**is_default** | **bool** | Is this election automatically applied in the absence of an election having been made.  May only be true for one election if multiple are provided. | [optional] 
**is_chosen** | **bool** | Is this the election that has been explicitly chosen from multiple options. | [optional] 
**consent_fee_price** | **float** | Optional. The consent fee paid per unit for granting consent. | [optional] 
**consent_fee_currency** | **str** | Optional. Currency of the consent fee. Required if a consent fee price is provided. | [optional] 
## Example

```python
from lusid.models.consent_granted_election import ConsentGrantedElection
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

election_key: StrictStr = "example_election_key"
is_default: Optional[StrictBool] = # Replace with your value
is_default:Optional[StrictBool] = None
is_chosen: Optional[StrictBool] = # Replace with your value
is_chosen:Optional[StrictBool] = None
consent_fee_price: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
consent_fee_currency: Optional[StrictStr] = "example_consent_fee_currency"
consent_granted_election_instance = ConsentGrantedElection(election_key=election_key, is_default=is_default, is_chosen=is_chosen, consent_fee_price=consent_fee_price, consent_fee_currency=consent_fee_currency)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

