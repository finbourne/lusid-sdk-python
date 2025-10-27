# SubHoldingKeyValueEquals

A criterion that checks whether a SubHoldingKey Value is equal to the given string value
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sub_holding_key** | **str** | The sub holding key whose value will form the left-hand side of the operation | 
**value** | **str** | The value to be compared against | 
**criterion_type** | **str** | The available values are: PropertyValueEquals, PropertyValueIn, SubHoldingKeyValueEquals | 
## Example

```python
from lusid.models.sub_holding_key_value_equals import SubHoldingKeyValueEquals
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

sub_holding_key: StrictStr = "example_sub_holding_key"
value: StrictStr = "example_value"
criterion_type: StrictStr = "example_criterion_type"
sub_holding_key_value_equals_instance = SubHoldingKeyValueEquals(sub_holding_key=sub_holding_key, value=value, criterion_type=criterion_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

