# UpdateIdentifierDefinitionRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hierarchy_level** | **str** | Optional metadata associated with the identifier definition. | [optional] 
**display_name** | **str** | A display name for the identifier. E.g. Figi. | [optional] 
**description** | **str** | An optional description for the identifier. | [optional] 
**properties** | [**Dict[str, ModelProperty]**](ModelProperty.md) | A set of properties for the identifier definition. | [optional] 
## Example

```python
from lusid.models.update_identifier_definition_request import UpdateIdentifierDefinitionRequest
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, constr, validator

hierarchy_level: Optional[StrictStr] = "example_hierarchy_level"
display_name: Optional[StrictStr] = "example_display_name"
description: Optional[StrictStr] = "example_description"
properties: Optional[Dict[str, ModelProperty]] = # Replace with your value
update_identifier_definition_request_instance = UpdateIdentifierDefinitionRequest(hierarchy_level=hierarchy_level, display_name=display_name, description=description, properties=properties)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

