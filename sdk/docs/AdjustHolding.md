# AdjustHolding

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**version** | [**Version**](Version.md) |  | 
**metadata** | **Dict[str, Optional[List[ResponseMetaData]]]** | Contains warnings related to unresolved instruments | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.adjust_holding import AdjustHolding
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

href: Optional[StrictStr] = "example_href"
version: Version
metadata: Optional[Dict[str, Optional[List[ResponseMetaData]]]] = # Replace with your value
links: Optional[List[Link]] = None
adjust_holding_instance = AdjustHolding(href=href, version=version, metadata=metadata, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

