# OrderBySpec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The key that uniquely identifies a queryable address in Lusid. | 
**sort_order** | **str** | The available values are: Ascending, Descending | 
## Example

```python
from lusid.models.order_by_spec import OrderBySpec
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

key: StrictStr = "example_key"
sort_order: StrictStr = "example_sort_order"
order_by_spec_instance = OrderBySpec(key=key, sort_order=sort_order)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

