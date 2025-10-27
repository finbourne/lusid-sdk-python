# UpsertIndexConventionRequest

Index convention that is to be stored in the convention data store.  Only one of these must be present.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**index_convention** | [**IndexConvention**](IndexConvention.md) |  | [optional] 
## Example

```python
from lusid.models.upsert_index_convention_request import UpsertIndexConventionRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

index_convention: Optional[IndexConvention] = # Replace with your value
upsert_index_convention_request_instance = UpsertIndexConventionRequest(index_convention=index_convention)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

