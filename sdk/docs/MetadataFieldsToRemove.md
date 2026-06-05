# MetadataFieldsToRemove

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata_fields** | **List[str]** | An array of FieldName(s) to be removed from the metadata field schema. | [optional] 
## Example

```python
from lusid.models.metadata_fields_to_remove import MetadataFieldsToRemove
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

metadata_fields: Optional[List[StrictStr]] = # Replace with your value
metadata_fields_to_remove_instance = MetadataFieldsToRemove(metadata_fields=metadata_fields)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

