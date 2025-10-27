# ComparisonAttributeValuePair

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute_name** | **str** | Comparison rule attribute name. | 
**value** | **str** | Computed value for the comparison rule attribute. | [optional] 
## Example

```python
from lusid.models.comparison_attribute_value_pair import ComparisonAttributeValuePair
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

attribute_name: StrictStr = "example_attribute_name"
value: Optional[StrictStr] = "example_value"
comparison_attribute_value_pair_instance = ComparisonAttributeValuePair(attribute_name=attribute_name, value=value)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

