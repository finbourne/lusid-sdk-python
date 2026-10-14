# FundStructureCloseRequest

The request to close a fund structure: finalise the named valuation point on every member, members first.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**valuation_point_code** | **str** | The code of the valuation point to finalise on every member fund. | 
**nav_type_code** | **str** | The NAV type to finalise under. Defaults to each fund&#39;s primary NAV type. | [optional] 
## Example

```python
from lusid.models.fund_structure_close_request import FundStructureCloseRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

valuation_point_code: StrictStr = "example_valuation_point_code"
nav_type_code: Optional[StrictStr] = "example_nav_type_code"
fund_structure_close_request_instance = FundStructureCloseRequest(valuation_point_code=valuation_point_code, nav_type_code=nav_type_code)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

