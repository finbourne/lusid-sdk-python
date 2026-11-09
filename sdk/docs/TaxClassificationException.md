# TaxClassificationException

Why an instrument could not be classified, or a flip of the qualifying-investments test a reviewer must see.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | MissingInputs, ConflictingSetup, ConflictingOverride or QualifyingInvestmentsCrossing. Available values: MissingInputs, ConflictingSetup, ConflictingOverride, QualifyingInvestmentsCrossing. | 
**code** | **str** | The stable code of the exception, for filtering and routing. | 
**message** | **str** | A description of why the instrument could not be classified or why the crossing was raised. | 
## Example

```python
from lusid.models.tax_classification_exception import TaxClassificationException
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

kind: StrictStr = "example_kind"
code: StrictStr = "example_code"
message: StrictStr = "example_message"
tax_classification_exception_instance = TaxClassificationException(kind=kind, code=code, message=message)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

