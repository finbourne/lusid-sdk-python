# RecipeComposer

Recipe composer is an object used to dynamically compose Configuration Recipe from atomic operations.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scope** | **str** | The scope used when updating or inserting the Recipe Composer. | 
**code** | **str** | User given string name (code) to identify the recipe. | 
**operations** | [**List[RecipeBlock]**](RecipeBlock.md) | Atomic operations used to compose a Configuration Recipe. | [optional] 
## Example

```python
from lusid.models.recipe_composer import RecipeComposer
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

scope: StrictStr = "example_scope"
code: StrictStr = "example_code"
operations: Optional[List[RecipeBlock]] = # Replace with your value
recipe_composer_instance = RecipeComposer(scope=scope, code=code, operations=operations)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

