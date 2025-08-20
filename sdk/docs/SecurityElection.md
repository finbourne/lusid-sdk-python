# SecurityElection

Security election for Events that result in equity
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**election_key** | **str** | Unique key associated to this election. | 
**is_chosen** | **bool** | Is this the election that has been explicitly chosen from multiple options. | [optional] 
**is_default** | **bool** | Is this election automatically applied in the absence of an election having been made. May only be true for one election if multiple are provided. | [optional] 
**price** | **float** | Price per unit of the security. At least one of UnitsRatio or Price must be provided. Price must non-zero. | [optional] 
**units_ratio** | [**UnitsRatio**](UnitsRatio.md) |  | [optional] 
## Example

```python
from lusid.models.security_election import SecurityElection
from typing import Any, Dict, Optional, Union
from pydantic.v1 import BaseModel, Field, StrictBool, StrictFloat, StrictInt, constr

election_key: StrictStr = "example_election_key"
is_chosen: Optional[StrictBool] = # Replace with your value
is_chosen:Optional[StrictBool] = None
is_default: Optional[StrictBool] = # Replace with your value
is_default:Optional[StrictBool] = None
price: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
units_ratio: Optional[UnitsRatio] = # Replace with your value
security_election_instance = SecurityElection(election_key=election_key, is_chosen=is_chosen, is_default=is_default, price=price, units_ratio=units_ratio)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

