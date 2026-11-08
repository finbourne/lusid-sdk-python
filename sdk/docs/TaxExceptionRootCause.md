# TaxExceptionRootCause

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | A stable code for the cause, for example PoolOutOfSync or MissingTreatmentLeaf. | 
**label** | **str** | A display label for the cause. | 
## Example

```python
from lusid.models.tax_exception_root_cause import TaxExceptionRootCause
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

code: StrictStr = "example_code"
label: StrictStr = "example_label"
tax_exception_root_cause_instance = TaxExceptionRootCause(code=code, label=label)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

