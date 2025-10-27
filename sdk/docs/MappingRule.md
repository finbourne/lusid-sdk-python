# MappingRule

An individual mapping rule, for mapping between a left and right field/property.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**left** | **str** | The name of the field/property in the left resource (e.g. a transaction) | [optional] 
**right** | **str** | The name of the field/property in the right resource (e.g. a transaction) | [optional] 
**comparison_type** | **str** | The type of comparison to be performed | [optional] 
**comparison_value** | **float** | The (optional) value used with ComparisonType. | [optional] 
**weight** | **float** | A factor used to influence the importance of this item. | [optional] 
**mapped_strings** | [**List[MappedString]**](MappedString.md) | The (optional) value used to map string values. | [optional] 
**is_case_sensitive** | **bool** | Should string comparisons take case into account, defaults to &#x60;false&#x60;. | [optional] 
## Example

```python
from lusid.models.mapping_rule import MappingRule
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

left: Optional[StrictStr] = "example_left"
right: Optional[StrictStr] = "example_right"
comparison_type: Optional[StrictStr] = "example_comparison_type"
comparison_value: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
weight: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
mapped_strings: Optional[List[MappedString]] = # Replace with your value
is_case_sensitive: Optional[StrictBool] = # Replace with your value
is_case_sensitive:Optional[StrictBool] = None
mapping_rule_instance = MappingRule(left=left, right=right, comparison_type=comparison_type, comparison_value=comparison_value, weight=weight, mapped_strings=mapped_strings, is_case_sensitive=is_case_sensitive)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

