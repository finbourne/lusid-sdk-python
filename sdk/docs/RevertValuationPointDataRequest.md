# RevertValuationPointDataRequest

The RevertValuationPointDataRequest.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**diary_entry_code** | **str** | Unique code for the Valuation Point. | 
## Example

```python
from lusid.models.revert_valuation_point_data_request import RevertValuationPointDataRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

diary_entry_code: StrictStr = "example_diary_entry_code"
revert_valuation_point_data_request_instance = RevertValuationPointDataRequest(diary_entry_code=diary_entry_code)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

