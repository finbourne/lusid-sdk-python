# BucketDefinition

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bucket_id** | **str** |  | 
**display_name** | **str** |  | 
**filter_expression** | **str** |  | 
**bucket_type** | **str** | Available values: Dealing, PnL, Fees, BalanceSheet, Misc. | 
**unitised** | **bool** |  | [optional] 
## Example

```python
from lusid.models.bucket_definition import BucketDefinition
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

bucket_id: StrictStr = "example_bucket_id"
display_name: StrictStr = "example_display_name"
filter_expression: StrictStr = "example_filter_expression"
bucket_type: StrictStr = "example_bucket_type"
unitised: Optional[StrictBool] = None
unitised:Optional[StrictBool] = None
bucket_definition_instance = BucketDefinition(bucket_id=bucket_id, display_name=display_name, filter_expression=filter_expression, bucket_type=bucket_type, unitised=unitised)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

