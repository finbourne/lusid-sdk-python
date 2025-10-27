# UpdateDataTypeRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | The display name of the data type. | [optional] 
**description** | **str** | The description of the data type. | [optional] 
**acceptable_values** | **List[str]** | The acceptable set of values for this data type. Only applies to &#39;open&#39; value type range. | [optional] 
**acceptable_units** | [**List[UpdateUnitRequest]**](UpdateUnitRequest.md) | The definitions of the acceptable units. | [optional] 
## Example

```python
from lusid.models.update_data_type_request import UpdateDataTypeRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

display_name: Optional[StrictStr] = "example_display_name"
description: Optional[StrictStr] = "example_description"
acceptable_values: Optional[List[StrictStr]] = # Replace with your value
acceptable_units: Optional[List[UpdateUnitRequest]] = # Replace with your value
update_data_type_request_instance = UpdateDataTypeRequest(display_name=display_name, description=description, acceptable_values=acceptable_values, acceptable_units=acceptable_units)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

