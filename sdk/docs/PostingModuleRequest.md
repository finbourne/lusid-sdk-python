# PostingModuleRequest

A Posting Module request definition
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | The code of the Posting Module. | 
**display_name** | **str** | The name of the Posting Module. | 
**description** | **str** | A description for the Posting Module. | [optional] 
**rules** | [**List[PostingModuleRule]**](PostingModuleRule.md) | The Posting Rules that apply for the Posting Module. Rules are evaluated in the order they occur in this collection. | [optional] 
## Example

```python
from lusid.models.posting_module_request import PostingModuleRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

code: StrictStr = "example_code"
display_name: StrictStr = "example_display_name"
description: Optional[StrictStr] = "example_description"
rules: Optional[List[PostingModuleRule]] = # Replace with your value
posting_module_request_instance = PostingModuleRequest(code=code, display_name=display_name, description=description, rules=rules)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

