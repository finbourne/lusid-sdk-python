# TransactionTypeCalculation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of calculation to perform | 
**side** | **str** | The side to which the calculation is applied | [optional] 
**formula** | **str** | The formula used to derive the total consideration amount when it is not provided on the transaction | [optional] 
## Example

```python
from lusid.models.transaction_type_calculation import TransactionTypeCalculation
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

type: StrictStr = "example_type"
side: Optional[StrictStr] = "example_side"
formula: Optional[StrictStr] = "example_formula"
transaction_type_calculation_instance = TransactionTypeCalculation(type=type, side=side, formula=formula)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

