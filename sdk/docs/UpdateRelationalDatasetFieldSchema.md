# UpdateRelationalDatasetFieldSchema

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**add** | [**RelationalDatasetFieldsToAdd**](RelationalDatasetFieldsToAdd.md) |  | [optional] 
**update** | [**RelationalDatasetFieldsToUpdate**](RelationalDatasetFieldsToUpdate.md) |  | [optional] 
**remove** | [**RelationalDatasetFieldsToRemove**](RelationalDatasetFieldsToRemove.md) |  | [optional] 
## Example

```python
from lusid.models.update_relational_dataset_field_schema import UpdateRelationalDatasetFieldSchema
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

add: Optional[RelationalDatasetFieldsToAdd] = None
update: Optional[RelationalDatasetFieldsToUpdate] = None
remove: Optional[RelationalDatasetFieldsToRemove] = None
update_relational_dataset_field_schema_instance = UpdateRelationalDatasetFieldSchema(add=add, update=update, remove=remove)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

