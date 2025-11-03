# UpdateSeriesIdentifierField

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field_name** | **str** | The unique identifier for the field within the dataset. | 
**display_name** | **str** | A user-friendly display name for the field. | [optional] 
**description** | **str** | A detailed description of the field and its purpose. | [optional] 
**data_type_id** | [**ResourceId**](ResourceId.md) |  | 
**required** | **bool** | Whether this field is mandatory in the dataset. | 
## Example

```python
from lusid.models.update_series_identifier_field import UpdateSeriesIdentifierField
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

field_name: StrictStr = "example_field_name"
display_name: Optional[StrictStr] = "example_display_name"
description: Optional[StrictStr] = "example_description"
data_type_id: ResourceId = # Replace with your value
required: StrictBool = # Replace with your value
required:StrictBool = True
update_series_identifier_field_instance = UpdateSeriesIdentifierField(field_name=field_name, display_name=display_name, description=description, data_type_id=data_type_id, required=required)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

