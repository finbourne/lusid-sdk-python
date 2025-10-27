# ResponseMetaData

Metadata related to an api response
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of meta data information being provided | [optional] 
**description** | **str** | The description of what occured for this specific piece of meta data | [optional] 
**identifier_type** | **str** | The type of the listed identifiers | [optional] 
**identifiers** | **List[str]** | The related identifiers that were impacted by this event | [optional] 
## Example

```python
from lusid.models.response_meta_data import ResponseMetaData
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

type: Optional[StrictStr] = "example_type"
description: Optional[StrictStr] = "example_description"
identifier_type: Optional[StrictStr] = "example_identifier_type"
identifiers: Optional[List[StrictStr]] = # Replace with your value
response_meta_data_instance = ResponseMetaData(type=type, description=description, identifier_type=identifier_type, identifiers=identifiers)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

