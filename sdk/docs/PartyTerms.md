# PartyTerms

What one party posts under a margin item.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**threshold** | **float** | The exposure that is tolerated before margin is called. Empty means no threshold. | [optional] 
**independent_amount** | **float** | The independent amount posted in addition to variation margin. | 
**cash_interest** | [**CashInterest**](CashInterest.md) |  | [optional] 
## Example

```python
from lusid.models.party_terms import PartyTerms
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

threshold: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
independent_amount: Union[StrictFloat, StrictInt] = # Replace with your value
cash_interest: Optional[CashInterest] = # Replace with your value
party_terms_instance = PartyTerms(threshold=threshold, independent_amount=independent_amount, cash_interest=cash_interest)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

