# UpsertRecipeRequest

A recipe or recipe snippet that is to be stored in the recipe structured data store.  Only one of these must be present.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | User given string name (code) to identify the recipe or snippet for storage in and retrieval from the data store.  Sensibly it would be expected to match the same code given inside the configuration recipe, if that is the element being stored,  though this is not enforced. In the case of a snippet for rules or options, again a sensible naming convention such as options_...  or marketrules_... is advocated to aid in ease of understanding when included elsewhere though not enforced. | 
**configuration_recipe** | [**ConfigurationRecipe**](ConfigurationRecipe.md) |  | [optional] 
**configuration_recipe_snippet** | [**ConfigurationRecipeSnippet**](ConfigurationRecipeSnippet.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


