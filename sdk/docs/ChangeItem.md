# ChangeItem

Information about a change to a field / property.  At least one of 'PreviousValue' or 'NewValue' will be set.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field_name** | **str** | The name of the field or property that has been changed. | 
**previous_value** | **str** | The previous value for this field / property. | [optional] 
**new_value** | **str** | The new value for this field / property. | [optional] 
**effective_from** | **datetime** | The market data time, i.e. the time to run the change from. | [optional] 
**effective_until** | **datetime** | The market data time, i.e. the time to run the change until. | [optional] 
## Example

```python
from lusid.models.change_item import ChangeItem
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, constr
from datetime import datetime
field_name: StrictStr = "example_field_name"
previous_value: Optional[StrictStr] = "example_previous_value"
new_value: Optional[StrictStr] = "example_new_value"
effective_from: Optional[datetime] = # Replace with your value
effective_until: Optional[datetime] = # Replace with your value
change_item_instance = ChangeItem(field_name=field_name, previous_value=previous_value, new_value=new_value, effective_from=effective_from, effective_until=effective_until)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

