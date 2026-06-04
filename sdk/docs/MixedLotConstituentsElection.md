# MixedLotConstituentsElection

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**election_key** | **str** |  | 
**is_default** | **bool** |  | [optional] 
**is_chosen** | **bool** |  | [optional] 
**securities_constituents** | [**List[SecurityOfferConstituent]**](SecurityOfferConstituent.md) |  | [optional] 
**cash_constituents** | [**List[CashOfferConstituent]**](CashOfferConstituent.md) |  | [optional] 
**cost_factor** | **float** |  | [optional] 
## Example

```python
from lusid.models.mixed_lot_constituents_election import MixedLotConstituentsElection
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

election_key: StrictStr = "example_election_key"
is_default: Optional[StrictBool] = # Replace with your value
is_default:Optional[StrictBool] = None
is_chosen: Optional[StrictBool] = # Replace with your value
is_chosen:Optional[StrictBool] = None
securities_constituents: Optional[List[SecurityOfferConstituent]] = # Replace with your value
cash_constituents: Optional[List[CashOfferConstituent]] = # Replace with your value
cost_factor: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
mixed_lot_constituents_election_instance = MixedLotConstituentsElection(election_key=election_key, is_default=is_default, is_chosen=is_chosen, securities_constituents=securities_constituents, cash_constituents=cash_constituents, cost_factor=cost_factor)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

