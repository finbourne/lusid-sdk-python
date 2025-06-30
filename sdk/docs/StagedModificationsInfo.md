# StagedModificationsInfo

The staged modifications metadata.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count_pending** | **int** | The number of staged modifications for the entity with a status of Pending for the requested asAt. | 
**href_pending** | **str** | Link to the list staged modifications endpoint, filtered by entityType, entityUniqueId and status (&#x3D; Pending). | 
**ids_previewed** | **List[str]** | An array of the ids of any StagedModifications being previewed. | [optional] 
## Example

```python
from lusid.models.staged_modifications_info import StagedModificationsInfo
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictInt, StrictStr, conlist

count_pending: StrictInt = # Replace with your value
count_pending: StrictInt = 42
href_pending: StrictStr = "example_href_pending"
ids_previewed: Optional[conlist(StrictStr)] = # Replace with your value
staged_modifications_info_instance = StagedModificationsInfo(count_pending=count_pending, href_pending=href_pending, ids_previewed=ids_previewed)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

