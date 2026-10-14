# FundStructureCloseResult

The outcome of closing a fund structure: one step per member in the order they were closed.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**structure_id** | [**ResourceId**](ResourceId.md) |  | 
**valuation_point_code** | **str** | The code of the valuation point to finalise on every member fund. | 
**steps** | [**List[FundStructureCloseStep]**](FundStructureCloseStep.md) | The finalisation of each member, in the order attempted. | 
**completed** | **bool** | Whether every member finalised. | 
## Example

```python
from lusid.models.fund_structure_close_result import FundStructureCloseResult
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

structure_id: ResourceId = # Replace with your value
valuation_point_code: StrictStr = "example_valuation_point_code"
steps: List[FundStructureCloseStep] = # Replace with your value
completed: StrictBool = # Replace with your value
completed:StrictBool = True
fund_structure_close_result_instance = FundStructureCloseResult(structure_id=structure_id, valuation_point_code=valuation_point_code, steps=steps, completed=completed)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

