# BucketBalanceFigures

A bucket's opening balance, activity and closing balance, which always satisfy opening + activity = closing.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**open** | **float** | The balance at the start of the bucket. | [optional] 
**activity** | **float** | The sum of the bucket&#39;s cash flows. | [optional] 
**close** | **float** | The balance at the end of the bucket: Open + Activity. | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.bucket_balance_figures import BucketBalanceFigures
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

open: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
activity: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
close: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
links: Optional[List[Link]] = None
bucket_balance_figures_instance = BucketBalanceFigures(open=open, activity=activity, close=close, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

