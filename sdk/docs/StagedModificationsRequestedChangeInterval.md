# StagedModificationsRequestedChangeInterval

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute_name** | **str** | Name of the property the change applies to. | [optional] 
**effective_range** | [**StagedModificationEffectiveRange**](StagedModificationEffectiveRange.md) |  | [optional] 
**previous_value** | [**PropertyValue**](PropertyValue.md) |  | [optional] 
**new_value** | [**PropertyValue**](PropertyValue.md) |  | [optional] 
**as_at_basis** | **str** | Whether the change represents the modification when the request was made or the modification as it would be at the latest time. | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid.models.staged_modifications_requested_change_interval import StagedModificationsRequestedChangeInterval
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

attribute_name: Optional[StrictStr] = "example_attribute_name"
effective_range: Optional[StagedModificationEffectiveRange] = # Replace with your value
previous_value: Optional[PropertyValue] = # Replace with your value
new_value: Optional[PropertyValue] = # Replace with your value
as_at_basis: Optional[StrictStr] = "example_as_at_basis"
links: Optional[List[Link]] = None
staged_modifications_requested_change_interval_instance = StagedModificationsRequestedChangeInterval(attribute_name=attribute_name, effective_range=effective_range, previous_value=previous_value, new_value=new_value, as_at_basis=as_at_basis, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

