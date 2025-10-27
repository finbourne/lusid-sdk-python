# FromRecipe

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scope** | **str** |  | [optional] 
**code** | **str** |  | [optional] 
## Example

```python
from lusid.models.from_recipe import FromRecipe
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

scope: Optional[StrictStr] = "example_scope"
code: Optional[StrictStr] = "example_code"
from_recipe_instance = FromRecipe(scope=scope, code=code)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

