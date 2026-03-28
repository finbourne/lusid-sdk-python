# WorkspacePermittedItemActions

The workspace item actions a user is permitted to perform within a workspace.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**read_item** | **bool** | Whether the user is permitted to read workspace items. | [optional] 
**add_item** | **bool** | Whether the user is permitted to add workspace items. | [optional] 
**update_item** | **bool** | Whether the user is permitted to update workspace items. | [optional] 
**delete_item** | **bool** | Whether the user is permitted to delete workspace items. | [optional] 
## Example

```python
from lusid.models.workspace_permitted_item_actions import WorkspacePermittedItemActions
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

read_item: Optional[StrictBool] = # Replace with your value
read_item:Optional[StrictBool] = None
add_item: Optional[StrictBool] = # Replace with your value
add_item:Optional[StrictBool] = None
update_item: Optional[StrictBool] = # Replace with your value
update_item:Optional[StrictBool] = None
delete_item: Optional[StrictBool] = # Replace with your value
delete_item:Optional[StrictBool] = None
workspace_permitted_item_actions_instance = WorkspacePermittedItemActions(read_item=read_item, add_item=add_item, update_item=update_item, delete_item=delete_item)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

