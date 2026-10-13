# CarryParameters

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**carry_rate** | **float** |  | 
**preferred_return_rate** | **float** |  | [optional] 
**catch_up_rate** | **float** |  | [optional] 
**waterfall_type** | **str** | Available values: WholeOfFund, DealByDeal. | [optional] 
## Example

```python
from lusid.models.carry_parameters import CarryParameters
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

carry_rate: Union[StrictFloat, StrictInt] = # Replace with your value
preferred_return_rate: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
catch_up_rate: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
waterfall_type: Optional[StrictStr] = "example_waterfall_type"
carry_parameters_instance = CarryParameters(carry_rate=carry_rate, preferred_return_rate=preferred_return_rate, catch_up_rate=catch_up_rate, waterfall_type=waterfall_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

