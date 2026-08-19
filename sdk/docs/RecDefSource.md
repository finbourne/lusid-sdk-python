# RecDefSource

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_type** | **str** | The type of entity that this source refers to. One of: Portfolio, PortfolioGroup, Fund. Available values: Portfolio, PortfolioGroup, Fund. | 
**id** | [**ResourceId**](ResourceId.md) |  | 
## Example

```python
from lusid.models.rec_def_source import RecDefSource
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

source_type: StrictStr = "example_source_type"
id: ResourceId
rec_def_source_instance = RecDefSource(source_type=source_type, id=id)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

