# UpdateRelationalDatasetFieldSchema

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**relational_dataset_fields_to_add** | [**RelationalDatasetFieldsToAdd**](RelationalDatasetFieldsToAdd.md) |  | [optional] 
**relational_dataset_fields_to_update** | [**RelationalDatasetFieldsToUpdate**](RelationalDatasetFieldsToUpdate.md) |  | [optional] 
**field_names_to_remove** | **List[str]** | An array of FieldName(s) to be removed from the FieldSchema. Only Value or Metadata fields can be removed. | [optional] 
## Example

```python
from lusid.models.update_relational_dataset_field_schema import UpdateRelationalDatasetFieldSchema
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

relational_dataset_fields_to_add: Optional[RelationalDatasetFieldsToAdd] = # Replace with your value
relational_dataset_fields_to_update: Optional[RelationalDatasetFieldsToUpdate] = # Replace with your value
field_names_to_remove: Optional[List[StrictStr]] = # Replace with your value
update_relational_dataset_field_schema_instance = UpdateRelationalDatasetFieldSchema(relational_dataset_fields_to_add=relational_dataset_fields_to_add, relational_dataset_fields_to_update=relational_dataset_fields_to_update, field_names_to_remove=field_names_to_remove)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

