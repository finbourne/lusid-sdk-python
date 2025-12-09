# CustomSortBy

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field_name** | **str** | The name of the field to sort by. | 
**priority_values** | **List[str]** | An optional list of priority field values to sort by, in the order they should be prioritized. | [optional] 
**remainder_order** | **str** | The sorting direction for the remaining field values. Either ascending (ASC) or descending (DESC). | 
## Example

```python
from lusid.models.custom_sort_by import CustomSortBy
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

field_name: StrictStr = "example_field_name"
priority_values: Optional[List[StrictStr]] = # Replace with your value
remainder_order: StrictStr = "example_remainder_order"
custom_sort_by_instance = CustomSortBy(field_name=field_name, priority_values=priority_values, remainder_order=remainder_order)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

