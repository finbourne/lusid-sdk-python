# LusidValidationProblemDetails

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**error_details** | **List[Dict[str, str]]** |  | [optional] 
**code** | **int** |  | 
**errors** | **Dict[str, List[str]]** |  | [optional] 
**type** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**status** | **int** |  | [optional] 
**detail** | **str** |  | [optional] 
**instance** | **str** |  | [optional] 
## Example

```python
from lusid.models.lusid_validation_problem_details import LusidValidationProblemDetails
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

name: StrictStr = "example_name"
error_details: Optional[List[Dict[str, StrictStr]]] = # Replace with your value
code: StrictInt
code: StrictInt = 42
errors: Optional[Dict[str, List[StrictStr]]] = None
type: Optional[StrictStr] = "example_type"
title: Optional[StrictStr] = "example_title"
status: Optional[StrictInt] = None
status: Optional[StrictInt] = None
detail: Optional[StrictStr] = "example_detail"
instance: Optional[StrictStr] = "example_instance"
lusid_validation_problem_details_instance = LusidValidationProblemDetails(name=name, error_details=error_details, code=code, errors=errors, type=type, title=title, status=status, detail=detail, instance=instance)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

