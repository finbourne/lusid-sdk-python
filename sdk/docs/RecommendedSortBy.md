# RecommendedSortBy

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute_name** | **str** | The property key, identifier type, or field to be sorted by. | 
**sort_order** | **str** | The sorting direction. Either ascending (ASC) or descending (DESC). | [optional] 
## Example

```python
from lusid.models.recommended_sort_by import RecommendedSortBy
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

attribute_name: StrictStr = "example_attribute_name"
sort_order: Optional[StrictStr] = "example_sort_order"
recommended_sort_by_instance = RecommendedSortBy(attribute_name=attribute_name, sort_order=sort_order)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

