# DateAttributes

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**irregular** | **bool** |  | 
**irregular_session** | **bool** |  | 
**new_hours** | **bool** |  | 
**activity** | **str** |  | [optional] 
**first_open** | **str** |  | [optional] 
**last_open** | **str** |  | [optional] 
**first_close** | **str** |  | [optional] 
**last_close** | **str** |  | [optional] 
## Example

```python
from lusid.models.date_attributes import DateAttributes
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, StrictBool, constr, validator

irregular: StrictBool = # Replace with your value
irregular:StrictBool = True
irregular_session: StrictBool = # Replace with your value
irregular_session:StrictBool = True
new_hours: StrictBool = # Replace with your value
new_hours:StrictBool = True
activity: Optional[StrictStr] = "example_activity"
first_open: Optional[StrictStr] = "example_first_open"
last_open: Optional[StrictStr] = "example_last_open"
first_close: Optional[StrictStr] = "example_first_close"
last_close: Optional[StrictStr] = "example_last_close"
date_attributes_instance = DateAttributes(irregular=irregular, irregular_session=irregular_session, new_hours=new_hours, activity=activity, first_open=first_open, last_open=last_open, first_close=first_close, last_close=last_close)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

