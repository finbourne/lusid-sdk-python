# MetadataFieldsToUpdate

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata_fields** | [**List[MetadataFieldDefinition]**](MetadataFieldDefinition.md) | The metadata field definitions for this configuration. | [optional] 
## Example

```python
from lusid.models.metadata_fields_to_update import MetadataFieldsToUpdate
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

metadata_fields: Optional[List[MetadataFieldDefinition]] = # Replace with your value
metadata_fields_to_update_instance = MetadataFieldsToUpdate(metadata_fields=metadata_fields)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

