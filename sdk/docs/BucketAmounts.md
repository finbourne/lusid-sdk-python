# BucketAmounts

An amount in the payment currency and, when a report currency was requested, in the report currency.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**local** | **float** | The amount in the payment currency. | [optional] 
**report_currency** | **float** | The amount in the report currency. Absent when no report currency was requested. | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.bucket_amounts import BucketAmounts
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

local: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
report_currency: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
links: Optional[List[Link]] = None
bucket_amounts_instance = BucketAmounts(local=local, report_currency=report_currency, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

