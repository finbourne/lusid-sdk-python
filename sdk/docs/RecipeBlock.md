# RecipeBlock

An atomic operation used in Recipe composer to compose a Configuration Recipe
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**RecipeValue**](RecipeValue.md) |  | [optional] 
**path** | **str** | Path of the Value that the operation is to be performed on. | [optional] 
**op** | **str** | Operation to be performed on the part of the value. | [optional] 
## Example

```python
from lusid.models.recipe_block import RecipeBlock
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

value: Optional[RecipeValue] = None
path: Optional[StrictStr] = "example_path"
op: Optional[StrictStr] = "example_op"
recipe_block_instance = RecipeBlock(value=value, path=path, op=op)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

