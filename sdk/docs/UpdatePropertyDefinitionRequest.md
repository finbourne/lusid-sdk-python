# UpdatePropertyDefinitionRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | The display name of the property. | 
**property_description** | **str** | Describes the property | [optional] 
## Example

```python
from lusid.models.update_property_definition_request import UpdatePropertyDefinitionRequest
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, constr

display_name: StrictStr = "example_display_name"
property_description: Optional[StrictStr] = "example_property_description"
update_property_definition_request_instance = UpdatePropertyDefinitionRequest(display_name=display_name, property_description=property_description)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

