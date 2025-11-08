# RelationalDatasetFieldsToRemove

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value_and_metadata_fields** | **List[str]** | An array of FieldName(s) to be removed from the FieldSchema. Only Value or Metadata fields can be removed. | [optional] 
## Example

```python
from lusid.models.relational_dataset_fields_to_remove import RelationalDatasetFieldsToRemove
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

value_and_metadata_fields: Optional[List[StrictStr]] = # Replace with your value
relational_dataset_fields_to_remove_instance = RelationalDatasetFieldsToRemove(value_and_metadata_fields=value_and_metadata_fields)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

