# UpsertRecipeRequest

A recipe that is to be stored in the recipe structured data store. Only one of these must be present.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**configuration_recipe** | [**ConfigurationRecipe**](ConfigurationRecipe.md) |  | [optional] 
## Example

```python
from lusid.models.upsert_recipe_request import UpsertRecipeRequest
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field

configuration_recipe: Optional[ConfigurationRecipe] = # Replace with your value
upsert_recipe_request_instance = UpsertRecipeRequest(configuration_recipe=configuration_recipe)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

