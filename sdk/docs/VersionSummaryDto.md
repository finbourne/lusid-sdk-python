# VersionSummaryDto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** |  | [optional] 
**build_version** | **str** |  | [optional] 
**excel_version** | **str** |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.version_summary_dto import VersionSummaryDto
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, conlist

api_version: Optional[StrictStr] = "example_api_version"
build_version: Optional[StrictStr] = "example_build_version"
excel_version: Optional[StrictStr] = "example_excel_version"
links: Optional[conlist(Link)] = None
version_summary_dto_instance = VersionSummaryDto(api_version=api_version, build_version=build_version, excel_version=excel_version, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

