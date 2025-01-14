# CustomDataModelCriteria


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conditions** | **str** | The conditions that the bound entity must meet to be valid. | [optional] 
**properties** | [**List[CustomDataModelPropertySpecificationWithDisplayName]**](CustomDataModelPropertySpecificationWithDisplayName.md) | The properties that are required or allowed on the bound entity. | [optional] 
**identifier_types** | [**List[CustomDataModelIdentifierTypeSpecificationWithDisplayName]**](CustomDataModelIdentifierTypeSpecificationWithDisplayName.md) | The identifier types that are required or allowed on the bound entity. | [optional] 
**attribute_aliases** | [**List[Alias]**](Alias.md) | The aliaes for property keys, identifier types, and fields on the bound entity. | [optional] 
**recommended_sort_by** | [**List[RecommendedSortBy]**](RecommendedSortBy.md) | The preferred default sorting instructions. | [optional] 

## Example

```python
from lusid.models.custom_data_model_criteria import CustomDataModelCriteria

# TODO update the JSON string below
json = "{}"
# create an instance of CustomDataModelCriteria from a JSON string
custom_data_model_criteria_instance = CustomDataModelCriteria.from_json(json)
# print the JSON string representation of the object
print CustomDataModelCriteria.to_json()

# convert the object into a dict
custom_data_model_criteria_dict = custom_data_model_criteria_instance.to_dict()
# create an instance of CustomDataModelCriteria from a dict
custom_data_model_criteria_form_dict = custom_data_model_criteria.from_dict(custom_data_model_criteria_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


