# FundPreviousNAV

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | The amount of the previous NAV. | [optional] 
## Example

```python
from lusid.models.fund_previous_nav import FundPreviousNAV
from typing import Any, Dict, Optional, Union
from pydantic.v1 import BaseModel, Field, StrictFloat, StrictInt

amount: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
fund_previous_nav_instance = FundPreviousNAV(amount=amount)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

