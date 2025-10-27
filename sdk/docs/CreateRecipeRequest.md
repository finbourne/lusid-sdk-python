# CreateRecipeRequest

Specification class to request for the creation/supplementing of a configuration recipe
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recipe_creation_market_data_scopes** | **List[str]** | The scopes in which the recipe creation would look for quotes/data. | 
**recipe_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**inline_recipe** | [**ConfigurationRecipe**](ConfigurationRecipe.md) |  | [optional] 
**as_at** | **datetime** | The asAt date to use | [optional] 
**effective_at** | **str** | The market data time, i.e. the recipe generated will look for rules with this effectiveAt. | 
## Example

```python
from lusid.models.create_recipe_request import CreateRecipeRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

recipe_creation_market_data_scopes: List[StrictStr] = # Replace with your value
recipe_id: Optional[ResourceId] = # Replace with your value
inline_recipe: Optional[ConfigurationRecipe] = # Replace with your value
as_at: Optional[datetime] = # Replace with your value
effective_at: StrictStr = "example_effective_at"
create_recipe_request_instance = CreateRecipeRequest(recipe_creation_market_data_scopes=recipe_creation_market_data_scopes, recipe_id=recipe_id, inline_recipe=inline_recipe, as_at=as_at, effective_at=effective_at)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

