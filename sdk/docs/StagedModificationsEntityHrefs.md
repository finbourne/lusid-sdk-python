# StagedModificationsEntityHrefs

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**when_staged** | **str** | The specific Uniform Resource Identifier (URI) for the staged modification change at the time when the change was requested. | [optional] 
**preview** | **str** | The specific Uniform Resource Identifier (URI) for the preview of staged modification change once applied. | [optional] 
**latest** | **str** | The specific Uniform Resource Identifier (URI) for the staged modification at latest time. | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.staged_modifications_entity_hrefs import StagedModificationsEntityHrefs
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

when_staged: Optional[StrictStr] = "example_when_staged"
preview: Optional[StrictStr] = "example_preview"
latest: Optional[StrictStr] = "example_latest"
links: Optional[List[Link]] = None
staged_modifications_entity_hrefs_instance = StagedModificationsEntityHrefs(when_staged=when_staged, preview=preview, latest=latest, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

