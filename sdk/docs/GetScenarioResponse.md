# GetScenarioResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** |  | [optional] 
**value** | [**ScenarioDefinition**](ScenarioDefinition.md) |  | [optional] 
**version** | [**Version**](Version.md) |  | [optional] 
**failed** | [**ErrorDetail**](ErrorDetail.md) |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.get_scenario_response import GetScenarioResponse
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

href: Optional[StrictStr] = "example_href"
value: Optional[ScenarioDefinition] = None
version: Optional[Version] = None
failed: Optional[ErrorDetail] = None
links: Optional[List[Link]] = None
get_scenario_response_instance = GetScenarioResponse(href=href, value=value, version=version, failed=failed, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

