# DataModelSummary

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ResourceId**](ResourceId.md) |  | 
**display_name** | **str** | The name of the Custom Data Model. | 
**description** | **str** | A description for the Custom Data Model. | 
**entity_type** | **str** | The entity type that the Custom Data Model binds to. | 
**type** | **str** | Either Root or Leaf or Intermediate. | 
**precedence** | **int** | Where in the hierarchy this model sits. | 
**children** | [**List[DataModelSummary]**](DataModelSummary.md) | Child Custom Data Models that will inherit from this data model. | 
## Example

```python
from lusid.models.data_model_summary import DataModelSummary
from typing import Any, Dict, List
from pydantic.v1 import BaseModel, Field, StrictInt, conlist, constr

id: ResourceId = # Replace with your value
display_name: StrictStr = "example_display_name"
description: StrictStr = "example_description"
entity_type: StrictStr = "example_entity_type"
type: StrictStr = "example_type"
precedence: StrictInt = # Replace with your value
precedence: StrictInt = 42
children: conlist(DataModelSummary) = # Replace with your value
data_model_summary_instance = DataModelSummary(id=id, display_name=display_name, description=description, entity_type=entity_type, type=type, precedence=precedence, children=children)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

