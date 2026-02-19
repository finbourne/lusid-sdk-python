# FeeCalculationRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**formula** | **str** |  | 
## Example

```python
from lusid.models.fee_calculation_request import FeeCalculationRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

formula: StrictStr = "example_formula"
fee_calculation_request_instance = FeeCalculationRequest(formula=formula)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

