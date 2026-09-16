# ApportionmentInput

One named amount that contributed to a member share class's apportionment base value - the workings behind  the figure rather than the figure alone. A member's inputs always sum to its base value.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | The input&#39;s identifier within its apportionment method, for example &#39;openingNav&#39;. | 
**display_name** | **str** | The input&#39;s human-readable name, for example &#39;Opening NAV&#39;. | 
**value** | **float** | The input&#39;s contribution to the base value, signed as it contributes. | 
## Example

```python
from lusid.models.apportionment_input import ApportionmentInput
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

code: StrictStr = "example_code"
display_name: StrictStr = "example_display_name"
value: Union[StrictFloat, StrictInt] = # Replace with your value
apportionment_input_instance = ApportionmentInput(code=code, display_name=display_name, value=value)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

