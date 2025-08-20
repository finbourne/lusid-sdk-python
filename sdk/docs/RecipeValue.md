# RecipeValue

Recipe value represents a data that is then used to perform an atomic operation which is then used in composition of Configuration Recipe. This object either includes the data itself (in json form or as simple string) or is a reference where the data can be obtained from (from a Configuration Recipe say). Only one field is to be populated.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**as_json** | **str** | Field to allow providing a potentially complex json value. | [optional] 
**as_string** | **str** | For simple value, a single input value, note complex nested objects are not allowed here. | [optional] 
**from_recipe** | [**FromRecipe**](FromRecipe.md) |  | [optional] 
## Example

```python
from lusid.models.recipe_value import RecipeValue
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, StrictStr

as_json: Optional[StrictStr] = "example_as_json"
as_string: Optional[StrictStr] = "example_as_string"
from_recipe: Optional[FromRecipe] = # Replace with your value
recipe_value_instance = RecipeValue(as_json=as_json, as_string=as_string, from_recipe=from_recipe)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

