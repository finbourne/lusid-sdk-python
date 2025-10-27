# ResourceListOfOrderInstruction

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | [**List[OrderInstruction]**](OrderInstruction.md) |  | 
**href** | **str** |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
**next_page** | **str** |  | [optional] 
**previous_page** | **str** |  | [optional] 
## Example

```python
from lusid.models.resource_list_of_order_instruction import ResourceListOfOrderInstruction
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

values: List[OrderInstruction]
href: Optional[StrictStr] = "example_href"
links: Optional[List[Link]] = None
next_page: Optional[StrictStr] = "example_next_page"
previous_page: Optional[StrictStr] = "example_previous_page"
resource_list_of_order_instruction_instance = ResourceListOfOrderInstruction(values=values, href=href, links=links, next_page=next_page, previous_page=previous_page)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

