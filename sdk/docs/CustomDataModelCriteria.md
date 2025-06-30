# CustomDataModelCriteria

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conditions** | **List[str]** | The conditions that the bound entity must meet to be valid. | [optional] 
**properties** | [**List[CustomDataModelPropertySpecificationWithDisplayName]**](CustomDataModelPropertySpecificationWithDisplayName.md) | The properties that are required or allowed on the bound entity. | [optional] 
**identifier_types** | [**List[CustomDataModelIdentifierTypeSpecificationWithDisplayName]**](CustomDataModelIdentifierTypeSpecificationWithDisplayName.md) | The identifier types that are required or allowed on the bound entity. | [optional] 
**attribute_aliases** | [**List[Alias]**](Alias.md) | The aliases for property keys, identifier types, and fields on the bound entity. | [optional] 
**recommended_sort_by** | [**List[RecommendedSortBy]**](RecommendedSortBy.md) | The preferred default sorting instructions. | [optional] 
## Example

```python
from lusid.models.custom_data_model_criteria import CustomDataModelCriteria
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, conlist

conditions: Optional[conlist(StrictStr)] = # Replace with your value
properties: Optional[conlist(CustomDataModelPropertySpecificationWithDisplayName)] = # Replace with your value
identifier_types: Optional[conlist(CustomDataModelIdentifierTypeSpecificationWithDisplayName)] = # Replace with your value
attribute_aliases: Optional[conlist(Alias)] = # Replace with your value
recommended_sort_by: Optional[conlist(RecommendedSortBy)] = # Replace with your value
custom_data_model_criteria_instance = CustomDataModelCriteria(conditions=conditions, properties=properties, identifier_types=identifier_types, attribute_aliases=attribute_aliases, recommended_sort_by=recommended_sort_by)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

