# BucketSetDefinition

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | 
**display_name** | **str** |  | 
**nav_types** | **List[str]** |  | [optional] 
**unitised** | **bool** |  | 
**buckets** | [**List[BucketDefinition]**](BucketDefinition.md) |  | 
## Example

```python
from lusid.models.bucket_set_definition import BucketSetDefinition
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

code: StrictStr = "example_code"
display_name: StrictStr = "example_display_name"
nav_types: Optional[List[StrictStr]] = # Replace with your value
unitised: StrictBool
unitised:StrictBool = True
buckets: List[BucketDefinition]
bucket_set_definition_instance = BucketSetDefinition(code=code, display_name=display_name, nav_types=nav_types, unitised=unitised, buckets=buckets)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

