# UpdateCustomDataModelRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | The name of the Custom Data Model. | 
**description** | **str** | A description for the Custom Data Model. | 
**parent_data_model** | [**ResourceId**](ResourceId.md) |  | [optional] 
**conditions** | **str** | The conditions that the bound entity must meet to be valid. | [optional] 
**properties** | [**List[CustomDataModelPropertySpecification]**](CustomDataModelPropertySpecification.md) | The properties that are required or allowed on the bound entity. | [optional] 
**identifier_types** | [**List[CustomDataModelIdentifierTypeSpecification]**](CustomDataModelIdentifierTypeSpecification.md) | The identifier types that are required or allowed on the bound entity. | [optional] 
**attribute_aliases** | [**List[Alias]**](Alias.md) | The aliases for property keys, identifier types, and fields on the bound entity. | [optional] 
**recommended_sort_by** | [**List[RecommendedSortBy]**](RecommendedSortBy.md) | The preferred default sorting instructions. | [optional] 
## Example

```python
from lusid.models.update_custom_data_model_request import UpdateCustomDataModelRequest
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, conlist, constr, validator

display_name: StrictStr = "example_display_name"
description: StrictStr = "example_description"
parent_data_model: Optional[ResourceId] = # Replace with your value
conditions: Optional[StrictStr] = "example_conditions"
properties: Optional[conlist(CustomDataModelPropertySpecification)] = # Replace with your value
identifier_types: Optional[conlist(CustomDataModelIdentifierTypeSpecification)] = # Replace with your value
attribute_aliases: Optional[conlist(Alias)] = # Replace with your value
recommended_sort_by: Optional[conlist(RecommendedSortBy)] = # Replace with your value
update_custom_data_model_request_instance = UpdateCustomDataModelRequest(display_name=display_name, description=description, parent_data_model=parent_data_model, conditions=conditions, properties=properties, identifier_types=identifier_types, attribute_aliases=attribute_aliases, recommended_sort_by=recommended_sort_by)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

