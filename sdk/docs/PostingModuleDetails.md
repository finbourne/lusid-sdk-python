# PostingModuleDetails

A posting Module request definition
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | The name of the Posting Module. | 
**description** | **str** | A description for the Posting Module. | [optional] 
**status** | **str** | The Posting Module status. Can be Active or Inactive. Defaults to Active. | 
## Example

```python
from lusid.models.posting_module_details import PostingModuleDetails
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

display_name: StrictStr = "example_display_name"
description: Optional[StrictStr] = "example_description"
status: StrictStr = "example_status"
posting_module_details_instance = PostingModuleDetails(display_name=display_name, description=description, status=status)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

