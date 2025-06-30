# ComparisonAttributeValuePair

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute_name** | **str** | Comparison rule attribute name. | 
**value** | **str** | Computed value for the comparison rule attribute. | [optional] 
## Example

```python
from lusid.models.comparison_attribute_value_pair import ComparisonAttributeValuePair
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, constr

attribute_name: StrictStr = "example_attribute_name"
value: Optional[StrictStr] = "example_value"
comparison_attribute_value_pair_instance = ComparisonAttributeValuePair(attribute_name=attribute_name, value=value)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

