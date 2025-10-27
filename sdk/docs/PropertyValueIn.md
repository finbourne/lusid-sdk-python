# PropertyValueIn

A criterion that checks whether a Property Value is equal to one of the given string values
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**property_key** | **str** | The property key whose value will form the left-hand side of the operation | 
**value** | **List[str]** | The value to be compared against | 
**criterion_type** | **str** | The available values are: PropertyValueEquals, PropertyValueIn, SubHoldingKeyValueEquals | 
## Example

```python
from lusid.models.property_value_in import PropertyValueIn
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

property_key: StrictStr = "example_property_key"
value: List[StrictStr] = # Replace with your value
criterion_type: StrictStr = "example_criterion_type"
property_value_in_instance = PropertyValueIn(property_key=property_key, value=value, criterion_type=criterion_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

