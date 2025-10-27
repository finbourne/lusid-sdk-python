# DataMapKey

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **str** | The version of the mappings. It is possible that a client will wish to update mappings over time. The version identifies the MAJOR.MINOR.PATCH version  of the mappings that the client assigns it. | [optional] 
**code** | **str** | A unique name to semantically identify the mapping set. | [optional] 
## Example

```python
from lusid.models.data_map_key import DataMapKey
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

version: Optional[StrictStr] = "example_version"
code: Optional[StrictStr] = "example_code"
data_map_key_instance = DataMapKey(version=version, code=code)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

