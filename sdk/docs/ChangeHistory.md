# ChangeHistory

A group of changes made by the same person at the same time.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** | The unique identifier of the user that made the change. | 
**modified_as_at** | **datetime** | The date/time of the change. | 
**request_id** | **str** | The unique identifier of the request that the changes were part of. | 
**action** | **str** | The action performed on the transaction, either created, updated, or deleted. The available values are: Create, Update, Delete | 
**changes** | [**List[ChangeItem]**](ChangeItem.md) | The collection of changes that were made. | 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.change_history import ChangeHistory
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, conlist, constr, validator
from datetime import datetime
user_id: StrictStr = "example_user_id"
modified_as_at: datetime = # Replace with your value
request_id: StrictStr = "example_request_id"
action: StrictStr = "example_action"
changes: conlist(ChangeItem) = # Replace with your value
links: Optional[conlist(Link)] = None
change_history_instance = ChangeHistory(user_id=user_id, modified_as_at=modified_as_at, request_id=request_id, action=action, changes=changes, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

