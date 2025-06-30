# UpdateCustomEntityDefinitionRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | A display label for the custom entity type. | 
**description** | **str** | A description for the custom entity type. | 
**field_schema** | [**List[CustomEntityFieldDefinition]**](CustomEntityFieldDefinition.md) | The description of the fields on the custom entity type. | 
## Example

```python
from lusid.models.update_custom_entity_definition_request import UpdateCustomEntityDefinitionRequest
from typing import Any, Dict, List
from pydantic.v1 import BaseModel, Field, conlist, constr, validator

display_name: StrictStr = "example_display_name"
description: StrictStr = "example_description"
field_schema: conlist(CustomEntityFieldDefinition) = # Replace with your value
update_custom_entity_definition_request_instance = UpdateCustomEntityDefinitionRequest(display_name=display_name, description=description, field_schema=field_schema)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

