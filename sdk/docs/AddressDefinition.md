# AddressDefinition

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | The display name of the address key. | [optional] 
**type** | **str** | The available values are: String, Int, Decimal, DateTime, Boolean, ResultValue, Result0D, Json | [optional] 
**description** | **str** | The description for this result. | [optional] 
**life_cycle_status** | **str** | What is the status of the address path. If it is not Production then it might be removed at some point in the future. See the removal date for the likely timing of that if any. | [optional] 
**removal_date** | **datetime** | If the life-cycle status of the address is Deprecated then this is the date at which support of the address will be suspended. After that date it will be removed at the earliest possible point subject to any specific contractual support and development constraints. | [optional] 
**documentation_link** | **str** | Contains a link to the documentation for this AddressDefinition in KnowledgeBase. | [optional] 
## Example

```python
from lusid.models.address_definition import AddressDefinition
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, validator
from datetime import datetime
display_name: Optional[StrictStr] = "example_display_name"
type: Optional[StrictStr] = "example_type"
description: Optional[StrictStr] = "example_description"
life_cycle_status: Optional[StrictStr] = "example_life_cycle_status"
removal_date: Optional[datetime] = # Replace with your value
documentation_link: Optional[StrictStr] = "example_documentation_link"
address_definition_instance = AddressDefinition(display_name=display_name, type=type, description=description, life_cycle_status=life_cycle_status, removal_date=removal_date, documentation_link=documentation_link)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

