# IdentifierForResolution

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier_key** | **str** | Identifier key in the format &#39;{domain}/{scope}/{code}&#39;. | 
## Example

```python
from lusid.models.identifier_for_resolution import IdentifierForResolution
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

identifier_key: StrictStr = "example_identifier_key"
identifier_for_resolution_instance = IdentifierForResolution(identifier_key=identifier_key)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

