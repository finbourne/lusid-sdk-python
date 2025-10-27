# UpdateRelationshipDefinitionRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | The display name of the relation. | 
**outward_description** | **str** | The description to relate source entity object and target entity object. | 
**inward_description** | **str** | The description to relate target entity object and source entity object. | 
## Example

```python
from lusid.models.update_relationship_definition_request import UpdateRelationshipDefinitionRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

display_name: StrictStr = "example_display_name"
outward_description: StrictStr = "example_outward_description"
inward_description: StrictStr = "example_inward_description"
update_relationship_definition_request_instance = UpdateRelationshipDefinitionRequest(display_name=display_name, outward_description=outward_description, inward_description=inward_description)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

