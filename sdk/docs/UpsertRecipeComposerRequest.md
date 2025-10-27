# UpsertRecipeComposerRequest

A recipe composer that is to be stored in the recipe composer data store or used for inline resolving.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recipe_composer** | [**RecipeComposer**](RecipeComposer.md) |  | [optional] 
## Example

```python
from lusid.models.upsert_recipe_composer_request import UpsertRecipeComposerRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

recipe_composer: Optional[RecipeComposer] = # Replace with your value
upsert_recipe_composer_request_instance = UpsertRecipeComposerRequest(recipe_composer=recipe_composer)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

