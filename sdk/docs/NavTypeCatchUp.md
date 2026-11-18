# NavTypeCatchUp

The number of valuation points the leader finalised while a follower NAV type was dormant (deactivated).
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nav_type_code** | **str** | The code of the follower NAV type that was reactivated. | 
**catch_up_count** | **int** | The number of valuation points the leader finalised while this follower NAV type was dormant (deactivated). | 
## Example

```python
from lusid.models.nav_type_catch_up import NavTypeCatchUp
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

nav_type_code: StrictStr = "example_nav_type_code"
catch_up_count: StrictInt = # Replace with your value
catch_up_count: StrictInt = 42
nav_type_catch_up_instance = NavTypeCatchUp(nav_type_code=nav_type_code, catch_up_count=catch_up_count)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

