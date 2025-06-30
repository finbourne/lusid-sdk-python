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
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, conlist, constr, validator

scope: StrictStr = "example_scope"
code: StrictStr = "example_code"
operations: Optional[conlist(RecipeBlock)] = # Replace with your value
recipe_composer_instance = RecipeComposer(scope=scope, code=code, operations=operations)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

