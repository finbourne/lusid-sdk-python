# AllocationGroup

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**classes** | [**List[AllocationGroupClass]**](AllocationGroupClass.md) | An optional list of share classes that belong to this group. Each entry must reference a ShareClass already present on the Fund. You can provide this or the Formula, but not both. | [optional] 
**code** | **str** | The unique code for the Allocation Group. Must be unique within the Fund. | 
**name** | **str** | The display name of the Allocation Group. | 
**description** | **str** | An optional description for the Allocation Group. | [optional] 
**share_class_short_code** | **str** | The short code that identifies the Allocation Group. | 
**apportionment_method_property** | [**ApportionmentMethodProperty**](ApportionmentMethodProperty.md) |  | [optional] 
**formula** | **str** | An optional filter expression used to define which classes belong to this group, based on fund grouping criteria. You can provide this or the Classes, but not both. | [optional] 
## Example

```python
from lusid.models.allocation_group import AllocationGroup
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

classes: Optional[List[AllocationGroupClass]] = # Replace with your value
code: StrictStr = "example_code"
name: StrictStr = "example_name"
description: Optional[StrictStr] = "example_description"
share_class_short_code: StrictStr = "example_share_class_short_code"
apportionment_method_property: Optional[ApportionmentMethodProperty] = # Replace with your value
formula: Optional[StrictStr] = "example_formula"
allocation_group_instance = AllocationGroup(classes=classes, code=code, name=name, description=description, share_class_short_code=share_class_short_code, apportionment_method_property=apportionment_method_property, formula=formula)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

