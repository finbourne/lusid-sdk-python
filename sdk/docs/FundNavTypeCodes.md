# FundNavTypeCodes

A fund resolved by a filtered fund list, with the NAV type codes matched by the list's hint.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fund_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**nav_type_codes** | **List[str]** |  | [optional] 
## Example

```python
from lusid.models.fund_nav_type_codes import FundNavTypeCodes
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

fund_id: Optional[ResourceId] = # Replace with your value
nav_type_codes: Optional[List[StrictStr]] = # Replace with your value
fund_nav_type_codes_instance = FundNavTypeCodes(fund_id=fund_id, nav_type_codes=nav_type_codes)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

