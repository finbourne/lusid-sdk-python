# ApportionmentMemberFactor

One member share class's outcome within an apportionment result: the base value the method produced for it  and the resulting apportionment factor.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**member_identifier** | **str** | The member share class&#39;s short code. | 
**fund_scope** | **str** | The scope of the fund the member share class belongs to. | [optional] 
**fund_code** | **str** | The code of the fund the member share class belongs to. | [optional] 
**base_value** | **float** | The base value the method produced for the member, or null for the SetFactor method. | [optional] 
**apportionment_factor** | **float** | The member&#39;s apportionment factor: its base value over the total across the group or fund. | 
## Example

```python
from lusid.models.apportionment_member_factor import ApportionmentMemberFactor
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

member_identifier: StrictStr = "example_member_identifier"
fund_scope: Optional[StrictStr] = "example_fund_scope"
fund_code: Optional[StrictStr] = "example_fund_code"
base_value: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
apportionment_factor: Union[StrictFloat, StrictInt] = # Replace with your value
apportionment_member_factor_instance = ApportionmentMemberFactor(member_identifier=member_identifier, fund_scope=fund_scope, fund_code=fund_code, base_value=base_value, apportionment_factor=apportionment_factor)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

