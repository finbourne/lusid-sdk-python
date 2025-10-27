# ComponentFilter

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter_id** | **str** |  | 
**filter** | **str** |  | 
## Example

```python
from lusid.models.component_filter import ComponentFilter
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

filter_id: StrictStr = "example_filter_id"
filter: StrictStr = "example_filter"
component_filter_instance = ComponentFilter(filter_id=filter_id, filter=filter)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

