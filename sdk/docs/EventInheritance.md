# EventInheritance

The information that determines the rules for instrument event inheritance.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parent_corporate_action_source_id** | [**ResourceId**](ResourceId.md) |  | 
## Example

```python
from lusid.models.event_inheritance import EventInheritance
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

parent_corporate_action_source_id: ResourceId = # Replace with your value
event_inheritance_instance = EventInheritance(parent_corporate_action_source_id=parent_corporate_action_source_id)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

